"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
import logging
from typing import TYPE_CHECKING, Callable

from serial import SerialException

from inverter_com.types import Result

if TYPE_CHECKING:  # pragma: nocover
    from inverter_com.inverter import Inverter


log = logging.getLogger(__file__)


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


def retry(func: Callable[["Inverter", str], Result]) -> Callable[["Inverter", str], Result]:
    def inner(cls: "Inverter", command: str) -> Result:
        for count in range(2):
            try:
                return func(cls, command)
            except SerialException:
                msg = "again" if count == 0 else "one last time"
                log.exception(f"Serial error, will try {msg}")

        # The last try
        return func(cls, command)

    return inner


def test_commands(port: str, *commands: str, debug: bool = False) -> None:
    import json

    from inverter_com import Inverter, constants

    if debug:  # pragma: nocover
        import logging

        logging.basicConfig(level=logging.DEBUG)

    inverter = Inverter(port)
    for command in commands:
        print(command)
        command = getattr(constants, f"CMD_{command.upper().replace('-', '_')}", command)
        res = inverter.send(command)
        print(json.dumps(res, indent=4, sort_keys=True))
        print()
