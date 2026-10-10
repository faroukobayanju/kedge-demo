from versions import latest, sort_tags


def test_latest_ignores_legacy():
    assert latest(["1.0", "nightly", "2.1", "1.10"]) == "2.1"


def test_sort_orders_numerically():
    assert sort_tags(["1.10", "1.2", "1.9"]) == ["1.2", "1.9", "1.10"]


def test_sort_puts_legacy_last():
    assert sort_tags(["beta", "1.0", "alpha"]) == ["1.0", "alpha", "beta"]
