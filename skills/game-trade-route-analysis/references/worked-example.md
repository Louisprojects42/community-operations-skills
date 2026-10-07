# Synthetic CSV semantics

Columns: `route,buy_price,sell_price,capacity,stock,demand,budget,fixed_fee,sell_fee_rate,loop_minutes,as_of`.

Prices and budget share one in-game currency; capacity/stock/demand are whole cargo units; sell_fee_rate is a decimal fraction. fixed_fee is paid from the available budget before buying. loop_minutes includes the complete repeatable loop. as_of is a timezone-aware ISO timestamp. No missing numeric field is treated as unlimited.

Example: buy 10, sell 14, capacity 100, stock 80, demand 60, budget 500, fixed fee 20, sale fee 0.05, loop 30 minutes. Affordable quantity is floor((500-20)/10)=48. Net profit is 48*14*(1-0.05)-48*10-20=138.40; hourly rate is 276.80.

These are fictional data, not game quotes. A source-age field records freshness; it does not certify that a market remains available. No expected-loss or confidence adjustment is performed.
