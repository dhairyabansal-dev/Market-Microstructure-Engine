import pytest

from market_microstructure.costs import bps_cost, implementation_shortfall


def test_implementation_shortfall_buy():
    assert implementation_shortfall(100, 101.5, 100, "buy") == 150


def test_implementation_shortfall_sell():
    assert implementation_shortfall(100, 98.5, 100, "sell") == 150


def test_bps_cost():
    assert bps_cost(150, 10_000) == 150


def test_invalid_side():
    with pytest.raises(ValueError):
        implementation_shortfall(100, 101, 10, "hold")
