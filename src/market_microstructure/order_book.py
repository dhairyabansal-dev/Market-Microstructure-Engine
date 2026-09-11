"""Order-book primitives and state management."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Quote:
    price: float
    size: float

    def __post_init__(self) -> None:
        if self.price <= 0 or self.size < 0:
            raise ValueError("price must be positive and size must be non-negative")


@dataclass(frozen=True)
class Trade:
    price: float
    size: float
    aggressor: str  # "buy" or "sell"

    def __post_init__(self) -> None:
        if self.price <= 0 or self.size <= 0:
            raise ValueError("trade price and size must be positive")
        if self.aggressor not in {"buy", "sell"}:
            raise ValueError("aggressor must be 'buy' or 'sell'")


@dataclass
class OrderBook:
    """Level-2 order book represented as price -> displayed size."""

    bids: dict[float, float] = field(default_factory=dict)
    asks: dict[float, float] = field(default_factory=dict)

    def update_bid(self, price: float, size: float) -> None:
        self._update(self.bids, price, size)

    def update_ask(self, price: float, size: float) -> None:
        self._update(self.asks, price, size)

    @staticmethod
    def _update(side: dict[float, float], price: float, size: float) -> None:
        if price <= 0 or size < 0:
            raise ValueError("price must be positive and size non-negative")
        if size == 0:
            side.pop(price, None)
        else:
            side[price] = size

    @property
    def best_bid(self) -> Quote | None:
        if not self.bids:
            return None
        p = max(self.bids)
        return Quote(p, self.bids[p])

    @property
    def best_ask(self) -> Quote | None:
        if not self.asks:
            return None
        p = min(self.asks)
        return Quote(p, self.asks[p])

    @property
    def mid_price(self) -> float | None:
        bid, ask = self.best_bid, self.best_ask
        if bid is None or ask is None:
            return None
        return (bid.price + ask.price) / 2
