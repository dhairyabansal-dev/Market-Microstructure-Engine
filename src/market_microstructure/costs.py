"""Transaction-cost and execution-quality calculations."""


def implementation_shortfall(
    decision_price: float,
    average_execution_price: float,
    quantity: float,
    side: str,
) -> float:
    """Return implementation shortfall in currency units."""
    if decision_price <= 0 or average_execution_price <= 0 or quantity < 0:
        raise ValueError("prices must be positive and quantity non-negative")
    if side == "buy":
        return (average_execution_price - decision_price) * quantity
    if side == "sell":
        return (decision_price - average_execution_price) * quantity
    raise ValueError("side must be 'buy' or 'sell'")


def bps_cost(cost: float, benchmark_notional: float) -> float:
    """Convert a monetary execution cost to basis points."""
    if benchmark_notional <= 0:
        raise ValueError("benchmark_notional must be positive")
    return cost / benchmark_notional * 10_000
