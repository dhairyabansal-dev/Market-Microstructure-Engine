"""Deterministic order-scheduling utilities."""


def twap_schedule(quantity: float, periods: int) -> list[float]:
    """Split a parent order evenly across periods."""
    _validate(quantity, periods)
    return [quantity / periods] * periods


def vwap_schedule(quantity: float, historical_volumes: list[float]) -> list[float]:
    """Allocate quantity proportionally to observed historical volume."""
    if quantity <= 0 or not historical_volumes:
        raise ValueError("quantity and volume history must be positive/non-empty")
    if any(v < 0 for v in historical_volumes) or sum(historical_volumes) <= 0:
        raise ValueError("volumes must be non-negative with positive total")
    total = sum(historical_volumes)
    return [quantity * v / total for v in historical_volumes]


def _validate(quantity: float, periods: int) -> None:
    if quantity <= 0:
        raise ValueError("quantity must be positive")
    if periods < 1:
        raise ValueError("periods must be >= 1")
