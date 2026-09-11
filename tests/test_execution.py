from market_microstructure import ExecutionModel, OrderBook


def test_buy_execution_consumes_ask_levels():
    book = OrderBook()
    book.update_bid(99.0, 100)
    book.update_ask(101.0, 50)
    book.update_ask(102.0, 100)

    report = ExecutionModel().execute_market_order(book, "buy", 100)

    assert report.filled_quantity == 100
    assert report.average_price == 101.5
    assert report.benchmark_price == 100.0
    assert report.slippage == 1.5
    assert report.implementation_shortfall == 150.0


def test_sell_execution_uses_bid_side():
    book = OrderBook()
    book.update_bid(99.0, 50)
    book.update_bid(98.0, 100)
    book.update_ask(101.0, 50)

    report = ExecutionModel().execute_market_order(book, "sell", 100)
    assert report.filled_quantity == 100
    assert report.average_price == 98.5
