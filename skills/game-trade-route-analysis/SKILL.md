---
name: game-trade-route-analysis
description: "Compare in-game commodity routes using cargo, budget, stock, demand, fees, travel time, and data freshness. Use for game economy tools; excludes real-money trading advice."
---

# Game Trade Route Analysis

Identify the game, patch/version, commodity units, currency, cargo constraint, available budget, and data timestamp. Prefer user-supplied market data or the game's current authorized data source. Never present a cached or synthetic price as a live quote. Keep game economy analysis distinct from purchases, real-money markets, or account actions.

Normalize buy and sell units before comparing margins. For one cargo type, constrain quantity by cargo capacity, available stock, destination demand, and affordable units after fixed upfront fees. Separate purchase cost, sale revenue, proportional fees, fixed trip cost, net profit, and total loop duration. Include loading, queues, and the return leg when the user wants repeatable hourly income.

Preserve unknown stock, demand, or duration as unknown. A missing demand value is not unlimited demand. Exclude infeasible routes or show scenario bounds with explicit assumptions. Report nominal profit separately from uncertainty; a confidence score is not a probability of success and should not multiply profit without a justified model.

The optional `scripts/rank_routes.py` computes deterministic single-commodity scenarios from a CSV. Run `python <skill-dir>/scripts/rank_routes.py <routes.csv>` after verifying its input semantics in [the worked example](references/worked-example.md). It uses exact decimal money arithmetic, whole cargo units, fixed upfront trip fees, and seller-side proportional fees. It has no API access and no risk model.

Compare profit per loop, profit per hour, budget required, bottleneck, and quote age. Test sensitivity to a plausible price change or delay if supplied. Explain when a fast lower-margin route beats a slow high-margin route. Mixed cargo, multi-leg credit recycling, uncertain losses, and partial sales require a different model; do not hide them in this simple calculation.

Deliver ranked feasible scenarios and their assumptions, retaining zero or negative-profit cases when diagnosing data.
