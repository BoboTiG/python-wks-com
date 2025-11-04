"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-wks-com
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import TYPE_CHECKING
from zoneinfo import ZoneInfo

from serial import SerialException

from wks_com import constants

if TYPE_CHECKING:  # pragma: nocover
    from collections.abc import Callable

    from wks_com._types import Result
    from wks_com.inverter import Inverter


log = logging.getLogger(__name__)


def compute_crc(value: str) -> str:
    """
    >>> compute_crc("(96332309100452")
    '?\xf3'
    """
    crc = 0
    for ch in value:
        crc ^= ord(ch) << 8
        for _ in range(8):
            crc = crc << 1 if (crc & 0x8000) == 0 else (crc << 1) ^ 0x1021
        crc &= 0xFFFF
    return crc.to_bytes(2, "big").decode(encoding="latin1")


def expand_command(command: str) -> str:
    """
    >>> expand_command("QPGS0")
    'QPGS0'

    >>> command = expand_command("QED")
    >>> command.startswith("QED")
    True
    >>> len(command) == len("QEDyyyymmdd")
    True

    >>> command = expand_command("QEM")
    >>> command.startswith("QEM")
    True
    >>> len(command) == len("QEMyyyymm")
    True

    >>> command = expand_command("QEY")
    >>> command.startswith("QEY")
    True
    >>> len(command) == len("QEYyyyy")
    True

    >>> command = expand_command("QLD")
    >>> command.startswith("QLD")
    True
    >>> len(command) == len("QLDyyyymmdd")
    True

    >>> command = expand_command("QLM")
    >>> command.startswith("QLM")
    True
    >>> len(command) == len("QLMyyyymm")
    True

    >>> command = expand_command("QLY")
    >>> command.startswith("QLY")
    True
    >>> len(command) == len("QLYyyyy")
    True
    """
    match command:
        case constants.CMD_DAILY_LOAD | constants.CMD_DAILY_PV:
            now = datetime.now(tz=ZoneInfo(constants.TIMEZONE))
            return f"{command}{now.strftime('%Y%m%d')}"
        case constants.CMD_MONTHLY_LOAD | constants.CMD_MONTHLY_PV:
            now = datetime.now(tz=ZoneInfo(constants.TIMEZONE))
            return f"{command}{now.strftime('%Y%m')}"
        case constants.CMD_YEARLY_LOAD | constants.CMD_YEARLY_PV:
            now = datetime.now(tz=ZoneInfo(constants.TIMEZONE))
            return f"{command}{now.strftime('%Y')}"
        case _:
            return command


def extract_response(seq: bytes) -> str:
    r"""
    >>> extract_response(b"(NAKss\r")
    'NAK'
    >>> extract_response(b"(96332309100452?\xf3\r")
    '96332309100452'
    """
    # Remove leading parenthesis, and trailing CRC + CR
    seq = seq[1:-3]
    return seq.decode(encoding="latin1")


def retry(func: Callable[[Inverter, str], Result]) -> Callable[[Inverter, str], Result]:
    def inner(cls: Inverter, command: str) -> Result:
        for count in range(2):
            try:
                return func(cls, command)
            except SerialException:  # noqa: PERF203
                msg = "again" if count == 0 else "one last time"
                log.exception("Serial error, will try %s", msg)

        # The last try
        return func(cls, command)

    return inner


def test_commands(port: str, *commands: str, debug: bool = False) -> None:  # noqa: PT028
    import json  # noqa: PLC0415

    from wks_com.inverter import Inverter  # noqa: PLC0415

    if debug:
        logging.basicConfig(level=logging.DEBUG)

    inverter = Inverter(port)
    for command in commands:
        print(command)
        cmd = getattr(constants, f"CMD_{command.upper().replace('-', '_')}", command)
        res = inverter.send(cmd)
        print(json.dumps(res, indent=4, sort_keys=True))
        print()
