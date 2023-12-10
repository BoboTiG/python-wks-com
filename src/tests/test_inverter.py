"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
from unittest.mock import patch

from inverter_com.inverter import Inverter


def test_read(port: str) -> None:
    def read_until(*_, **__):
        return b"foo\r"

    with patch("inverter_com.inverter.Inverter.send") as mocked:
        mocked.return_value = "XXX"
        inverter = Inverter(port)

    with patch.object(inverter._conn, "read_until", new=read_until):
        assert inverter.read() == b"foo\r"

    assert inverter.reads == 4
    assert inverter.writes == 0


def test_send(port: str) -> None:
    def read_until(*_, **__):
        return b"(fooXX\r"

    def write(seq: bytes):
        assert seq == b"cmd\x93o\r"
        return len(seq)

    with patch("inverter_com.inverter.Inverter.send") as mocked:
        mocked.return_value = "XXX"
        inverter = Inverter(port)

    with (
        patch.object(inverter._conn, "read_until", new=read_until),
        patch.object(inverter._conn, "write", new=write),
    ):
        assert inverter.send("cmd") == "foo"

    assert inverter.reads == 7
    assert inverter.writes == 6
    assert repr(inverter) == f"Inverter(port={port!r}, reads=7, serial_no='XXX', writes=6)"
    assert str(inverter) == f"Inverter(port={port!r}, reads=7, serial_no='XXX', writes=6)"


def test_write(port: str) -> None:
    def write(seq: bytes):
        assert seq == b"cmd\x93o\r"
        return len(seq)

    with patch("inverter_com.inverter.Inverter.send") as mocked:
        mocked.return_value = "XXX"
        inverter = Inverter(port)

    with patch.object(inverter._conn, "write", new=write):
        assert inverter.write("cmd")

    assert inverter.writes == 6
