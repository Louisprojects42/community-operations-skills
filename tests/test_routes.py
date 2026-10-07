import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1]/'skills/game-trade-route-analysis/scripts/rank_routes.py'
spec = importlib.util.spec_from_file_location('routes', PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def row(**changes):
    values = dict(route='Synthetic',buy_price='10',sell_price='14',capacity='100',stock='80',demand='60',budget='500',fixed_fee='20',sell_fee_rate='0.05',loop_minutes='30',as_of='2026-01-01T12:00:00+00:00')
    values.update(changes)
    return values

class RouteTests(unittest.TestCase):
    def test_budget_and_fees(self):
        result = module.rank_row(row())
        self.assertEqual(result['quantity'], 48)
        self.assertEqual(result['upfront_required'], '500.00')
        self.assertEqual(result['net_profit'], '138.40')
        self.assertEqual(result['profit_per_hour'], '276.80')
    def test_stock_demand_and_zero(self):
        self.assertEqual(module.rank_row(row(stock='3'))['quantity'], 3)
        self.assertEqual(module.rank_row(row(demand='2'))['quantity'], 2)
        result = module.rank_row(row(stock='0'))
        self.assertEqual(result['status'], 'infeasible')
        self.assertEqual(result['net_profit'], '0.00')
        self.assertEqual(module.rank_row(row(budget='10'))['quantity'], 0)
    def test_invalid_data_is_not_unlimited(self):
        for changes in ({'demand':''},{'stock':'NaN'},{'capacity':'1.5'},{'buy_price':'0'}, {'sell_fee_rate':'1.1'},{'loop_minutes':'0'},{'as_of':'2026-01-01'},{'budget':'Infinity'},{'fixed_fee':'-1'}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                module.rank_row(row(**changes))
    def test_negative_margin_and_large_money(self):
        self.assertTrue(module.rank_row(row(sell_price='9'))['net_profit'].startswith('-'))
        result = module.rank_row(row(buy_price='1000000000000000000',sell_price='1000000000000000000',budget='1000000000000000000',fixed_fee='0',sell_fee_rate='0'))
        self.assertEqual(result['quantity'], 1)
        self.assertEqual(result['net_profit'], '0.00')
