from versions import is_legacy, latest, sort_tags


def test_proper_version_not_legacy():
    assert not is_legacy("1.2.3")


def test_nightly_is_legacy():
    assert is_legacy("nightly")


def test_latest_ignores_legacy():
    assert latest(["1.0", "nightly", "2.1", "1.10"]) == "2.1"


def test_sort_orders_numerically():
    assert sort_tags(["1.10", "1.2", "1.9"]) == ["1.2", "1.9", "1.10"]


def test_sort_puts_legacy_last():
    assert sort_tags(["beta", "1.0", "alpha"]) == ["1.0", "alpha", "beta"]
