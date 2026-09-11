"""Simple execution and transaction-cost model."""

from dataclasses import dataclass

from .order_book import OrderBook


@dataclass(frozen=True)
class ExecutionReport:
    side: str
    quantity: float
    filled_quantity: float
    average_price: float | None
    benchmark_price: float | None
    slippage: float | None
    implementation_shortfall: float | None


class ExecutionModel:
    """Consume displayed top-of-book liquidity for a market order.

    This deliberately models only displayed liquidity. It is a transparent
    baseline, not a claim to reproduce a live matching engine.
    """

    def execute_market_order(self, book: OrderBook, side: str, quantity: float) -> ExecutionReport:
        if side not in {"buy", "sell"}:
            raise ValueError("side must be 'buy' or 'sell'")
        if quantity <= 0:
            raise ValueError("quantity must be positive")

        benchmark = book.mid_price
        levels = sorted(book.asks.items()) if side == "buy" else sorted(book.bids.items(), reverse=True)
        remaining = quantity
        notional = 0.0
        filled = 0.0

        for price, size in levels:
            take = min(remaining, size)
            notional += take * price
            filled += take
            remaining -= take
            if remaining <= 0:
                break

        average = notional / filled if filled else None
        slippage = None
        if average is not None and benchmark is not None:
            slippage = (average - benchmark) if side == "buy" else (benchmark - average)

        shortfall = slippage * filled if slippage is not None else None
        return ExecutionReport(side, quantity, filled, average, benchmark, slippage, shortfall)
