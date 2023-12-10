"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
import logging
from unittest.mock import patch

from serial import SerialException

from inverter_com.inverter import Inverter


def read_until(expected: str = "") -> bytes:
    return b"(fooXX\r"


def write(seq: bytes) -> int:
    assert seq == b"cmd\x93o\r"
    return len(seq)


def test_read(port: str) -> None:
    with patch("inverter_com.inverter.Inverter.send") as mocked:
        mocked.return_value = "XXX"
        inverter = Inverter(port)

    with patch.object(inverter._conn, "read_until", new=read_until):
        assert inverter.read() == b"(fooXX\r"

    assert inverter.reads == 7
    assert inverter.writes == 0


def test_send(port: str) -> None:
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


def test_send_retry(port: str, caplog) -> None:
    """
    When a script keeps the connection open (like when reading data on a regular basis),
    and then one does a second call on the same port from another script (or via the `inverter-*` executable),
    then such an eerror would likely happen:

        File "inverter.py", line 43, in read
          res = self._conn.read_until(expected=b"\r")
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/.../site-packages/serial/serialutil.py", line 663, in read_until
          c = self.read(1)
          ^^^^^^^^^^^^
        File "/h.../site-packages/serial/serialposix.py", line 595, in read
          raise SerialException(
        serial.serialutil.SerialException: device reports readiness to read but returned no data (device disconnected or multiple access on port?)

    This test ensures the retry mechanism will mitigate the behavior.
    """  # noqa[E501]
    count = 1

    def read_until_bad(expected: str = "") -> bytes:
        nonlocal count
        count += 1
        if count <= 3:
            raise SerialException("device reports readiness to read but returned no data")
        return read_until(expected=expected)

    with patch("inverter_com.inverter.Inverter.send") as mocked:
        mocked.return_value = "XXX"
        inverter = Inverter(port)

    with (
        patch.object(inverter._conn, "read_until", new=read_until_bad),
        patch.object(inverter._conn, "write", new=write),
    ):
        assert inverter.send("cmd") == "foo"

    assert inverter.reads == 7
    assert inverter.writes == 18

    errors_log = [record for record in caplog.records if record.levelno == logging.ERROR]
    assert len(errors_log) == 2


def test_write(port: str) -> None:
    with patch("inverter_com.inverter.Inverter.send") as mocked:
        mocked.return_value = "XXX"
        inverter = Inverter(port)

    with patch.object(inverter._conn, "write", new=write):
        assert inverter.write("cmd")

    assert inverter.writes == 6
