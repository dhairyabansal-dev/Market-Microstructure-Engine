"""Core market-microstructure metrics."""

from .order_book import OrderBook


def quoted_spread(book: OrderBook) -> float | None:
    """Absolute best bid/ask spread."""
    bid, ask = book.best_bid, book.best_ask
    if bid is None or ask is None:
        return None
    return ask.price - bid.price


def relative_spread(book: OrderBook) -> float | None:
    """Quoted spread divided by mid-price."""
    spread, mid = quoted_spread(book), book.mid_price
    if spread is None or mid is None or mid == 0:
        return None
    return spread / mid


def microprice(book: OrderBook) -> float | None:
    """Queue-size weighted mid-price using top-of-book liquidity."""
    bid, ask = book.best_bid, book.best_ask
    if bid is None or ask is None or bid.size + ask.size == 0:
        return None
    return (ask.price * bid.size + bid.price * ask.size) / (bid.size + ask.size)


def order_imbalance(book: OrderBook, levels: int = 1) -> float | None:
    """(bid depth - ask depth) / total depth over the top N levels."""
    if levels < 1:
        raise ValueError("levels must be >= 1")
    bids = sorted(book.bids.items(), reverse=True)[:levels]
    asks = sorted(book.asks.items())[:levels]
    bid_depth = sum(size for _, size in bids)
    ask_depth = sum(size for _, size in asks)
    total = bid_depth + ask_depth
    if total == 0:
        return None
    return (bid_depth - ask_depth) / total
