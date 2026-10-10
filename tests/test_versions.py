from versions import is_legacy


def test_proper_version_not_legacy():
    assert not is_legacy("1.2.3")


def test_nightly_is_legacy():
    assert is_legacy("nightly")
