from market_microstructure.strategies import twap_schedule, vwap_schedule


def test_twap():
    schedule = twap_schedule(1000, 4)
    assert schedule == [250.0] * 4
    assert sum(schedule) == 1000


def test_vwap():
    schedule = vwap_schedule(1000, [10, 20, 30, 40])
    assert schedule == [100.0, 200.0, 300.0, 400.0]
    assert sum(schedule) == 1000
