#!/usr/bin/env python3
"""Rank fictional/game routes from explicit CSV scenarios. No network access."""
import argparse
import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation, ROUND_FLOOR, ROUND_HALF_UP, localcontext
import json

NUMERIC = ('buy_price','sell_price','capacity','stock','demand','budget',
           'fixed_fee','sell_fee_rate','loop_minutes')
FIELDS = ('route',) + NUMERIC + ('as_of',)

def number(row, key):
    try:
        value = Decimal(row[key].strip())
    except (KeyError, AttributeError, InvalidOperation):
        raise ValueError('missing or invalid ' + key) from None
    if not value.is_finite() or value < 0 or value > Decimal('1e18'):
        raise ValueError(key + ' must be finite and between 0 and 1e18')
    return value

def rank_row(row):
    with localcontext() as ctx:
        ctx.prec = 80
        data = {key:number(row, key) for key in NUMERIC}
        if data['buy_price'] == 0 or data['loop_minutes'] == 0:
            raise ValueError('buy_price and loop_minutes must be positive')
        if data['sell_fee_rate'] > 1:
            raise ValueError('sell_fee_rate must be a fraction from 0 to 1')
        for key in ('capacity','stock','demand'):
            if data[key] != data[key].to_integral_value():
                raise ValueError(key + ' must be whole cargo units')
        route = row.get('route', '').strip()
        if not route:
            raise ValueError('route name is required')
        try:
            stamp = datetime.fromisoformat(row['as_of'].replace('Z', '+00:00'))
        except (KeyError, AttributeError, ValueError):
            raise ValueError('as_of must be a timezone-aware ISO timestamp') from None
        if stamp.tzinfo is None or stamp.utcoffset() is None:
            raise ValueError('as_of must include a timezone')
        affordable = max(Decimal(0), ((data['budget']-data['fixed_fee'])/data['buy_price']).to_integral_value(rounding=ROUND_FLOOR))
        limits = {key:data[key] for key in ('capacity','stock','demand')}
        limits['affordable'] = affordable
        quantity = int(min(limits.values()))
        purchase = quantity*data['buy_price']
        revenue = quantity*data['sell_price']
        sale_fee = revenue*data['sell_fee_rate']
        fixed_fee = data['fixed_fee'] if quantity else Decimal(0)
        net = revenue-sale_fee-purchase-fixed_fee
        def money(value):
            return str(value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        return {'route':route,'status':'feasible' if quantity else 'infeasible',
                'quantity':quantity,'bottlenecks':[key for key,val in limits.items() if val == quantity],
                'purchase_cost':money(purchase),'upfront_required':money(purchase+fixed_fee),
                'sale_revenue':money(revenue),'sale_fee':money(sale_fee),'fixed_fee':money(fixed_fee),
                'net_profit':money(net),'profit_per_hour':money(net*60/data['loop_minutes']),
                'as_of':stamp.isoformat(),'quote_verified_live':False}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_path')
    args = parser.parse_args()
    try:
        with open(args.csv_path, encoding='utf-8-sig', newline='') as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames is None or not set(FIELDS).issubset(reader.fieldnames):
                raise ValueError('CSV requires columns: ' + ','.join(FIELDS))
            rows = []
            for line, row in enumerate(reader, 2):
                try:
                    rows.append(rank_row(row))
                except ValueError as exc:
                    raise ValueError('row ' + str(line) + ': ' + str(exc)) from None
        rows.sort(key=lambda row:(row['status'] == 'feasible', Decimal(row['profit_per_hour'])), reverse=True)
        print(json.dumps(rows, indent=2))
    except (OSError, csv.Error, ValueError) as exc:
        parser.exit(2, str(exc) + '\n')
if __name__ == '__main__':
    main()
