from market_microstructure import OrderBook, microprice, order_imbalance, quoted_spread


def make_book() -> OrderBook:
    book = OrderBook()
    book.update_bid(99.0, 100)
    book.update_bid(98.0, 200)
    book.update_ask(101.0, 50)
    book.update_ask(102.0, 150)
    return book


def test_best_quotes_and_mid():
    book = make_book()
    assert book.best_bid.price == 99.0
    assert book.best_ask.price == 101.0
    assert book.mid_price == 100.0


def test_spread():
    assert quoted_spread(make_book()) == 2.0


def test_microprice_moves_toward_thinner_ask():
    assert microprice(make_book()) == 100.33333333333333


def test_order_imbalance():
    book = make_book()
    assert order_imbalance(book, levels=2) == 100 / 500
