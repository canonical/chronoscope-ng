from chronoscope import utils


def test_ns_uses_utc():
    assert utils.ns("1970-01-01T00:00:00.000000001") == 1


def test_unpack_event_id():
    event_id = 0x1ABC_0000_0000_0042

    assert utils.unpack_event_id(event_id) == (1, 0xABC, 0x42)
    assert utils.format_event_id(event_id) == "(1 2748 66)"
