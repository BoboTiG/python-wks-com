"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-wks-com
"""
import logging
from unittest.mock import patch

import pytest
from serial import SerialException

from wks_com import constants
from wks_com.inverter import Inverter


def read_until(expected: str = "") -> bytes:
    return b"(fooXX\r"


def write(seq: bytes) -> int:
    assert seq == b"cmd\x93o\r"
    return len(seq)


@pytest.fixture()
def inverter(port: str) -> Inverter:
    return Inverter(port)


def test_exclusive_access(inverter: Inverter) -> None:
    with pytest.raises(SerialException) as exc:
        Inverter(inverter.port)

    assert exc.value.errno == 11
    assert "Could not exclusively lock port" in exc.value.strerror
    assert inverter.reads == 0
    assert inverter.writes == 0


@pytest.mark.parametrize(
    "command, response, attr, expected",
    [
        (constants.CMD_MODEL, b"(MKS2-5600xx\r", "model", "MKS2-5600"),
        (constants.CMD_SERIAL_NO, b"(96332309100458xx\r", "serial_no", "96332309100458"),
        (
            constants.CMD_METRICS,
            (
                b"(0 96332309100452 L 00 227.7 50.01 227.7 50.01 1252 1245 022 00.8 "
                b"000 000 330.7 000 01252 01245 022 11102010 0 1 060 120 030 00 000xx\r"
            ),
            "serial_no",
            "96332309100452",
        ),
    ],
)
def test_decode(command: str, response: bytes, attr: str, expected: str, inverter: Inverter) -> None:
    assert getattr(inverter, attr) == ""
    inverter.decode(command, response)
    assert getattr(inverter, attr) == expected


def test_read(inverter: Inverter) -> None:
    with patch.object(inverter._conn, "read_until", new=read_until):
        assert inverter.read() == b"(fooXX\r"

    assert inverter.reads == 7
    assert inverter.writes == 0


def test_send(inverter: Inverter) -> None:
    with (
        patch.object(inverter._conn, "read_until", new=read_until),
        patch.object(inverter._conn, "write", new=write),
    ):
        assert inverter.send("cmd") == "foo"

    assert inverter.reads == 7
    assert inverter.writes == 6
    assert repr(inverter) == f"Inverter(port={inverter.port!r}, model='', reads=7, serial_no='', writes=6)"
    assert str(inverter) == f"Inverter(port={inverter.port!r}, model='', reads=7, serial_no='', writes=6)"


def test_send_retry(inverter: Inverter, caplog) -> None:
    """
    When a script keeps the connection open (like when reading data on a regular basis),
    and then one does a second call on the same port from another script (or via the `inverter-*` executable),
    then such an error would likely happen:

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

    with (
        patch.object(inverter._conn, "read_until", new=read_until_bad),
        patch.object(inverter._conn, "write", new=write),
    ):
        assert inverter.send("cmd") == "foo"

    assert inverter.reads == 7
    assert inverter.writes == 18

    errors_log = [record for record in caplog.records if record.levelno == logging.ERROR]
    assert len(errors_log) == 2


def test_write(inverter: Inverter) -> None:
    with patch.object(inverter._conn, "write", new=write):
        assert inverter.write("cmd")

    assert inverter.writes == 6
