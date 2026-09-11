from market_microstructure import ExecutionModel, OrderBook, microprice, order_imbalance, quoted_spread
from market_microstructure.strategies import twap_schedule, vwap_schedule


book = OrderBook()
for price, size in [(99.0, 100), (98.0, 200)]:
    book.update_bid(price, size)
for price, size in [(101.0, 50), (102.0, 150)]:
    book.update_ask(price, size)

print(f"Best bid: {book.best_bid}")
print(f"Best ask: {book.best_ask}")
print(f"Mid: {book.mid_price:.2f}")
print(f"Spread: {quoted_spread(book):.2f}")
print(f"Microprice: {microprice(book):.4f}")
print(f"2-level imbalance: {order_imbalance(book, 2):.4f}")

report = ExecutionModel().execute_market_order(book, "buy", 100)
print("\nExecution report:")
print(report)

print("\nTWAP:", twap_schedule(1000, 5))
print("VWAP:", vwap_schedule(1000, [10, 20, 30, 40]))
