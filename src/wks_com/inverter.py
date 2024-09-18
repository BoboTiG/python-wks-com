"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-wks-com
"""

import logging
from dataclasses import dataclass, field

import serial

from wks_com.constants import CMD_METRICS, CMD_MODEL, CMD_SERIAL_NO, DEFAULT_PORT
from wks_com.helpers import compute_crc, expand_command, extract_response, retry
from wks_com.types import Result
from wks_com.unpackers import unpack

log = logging.getLogger(__name__)


@dataclass
class Inverter:
    port: str = field(default=DEFAULT_PORT)
    baudrate: int = field(default=2400, repr=False, kw_only=True)
    bytesize: int = field(default=serial.EIGHTBITS, repr=False, kw_only=True)
    exclusive: bool = field(default=True, repr=False, kw_only=True)
    model: str = field(default="", kw_only=True)
    parity: str = field(default=serial.PARITY_NONE, repr=False, kw_only=True)
    reads: int = field(default=0, init=False)
    serial_no: str = field(default="", kw_only=True)
    stopbits: int = field(default=serial.STOPBITS_ONE, repr=False, kw_only=True)
    timeout: float | None = field(default=None, repr=False, kw_only=True)
    writes: int = field(default=0, init=False)

    _conn: serial.Serial = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._conn = serial.Serial(
            baudrate=self.baudrate,
            bytesize=self.bytesize,
            parity=self.parity,
            port=self.port,
            stopbits=self.stopbits,
            exclusive=self.exclusive,
            timeout=self.timeout,
        )

    def decode(self, command: str, response: bytes) -> Result:
        res = unpack(command, extract_response(response))
        log.debug("%s < DECODED %r", self._conn.port, res)

        if command == CMD_MODEL:
            self.model = str(res)
        elif command == CMD_SERIAL_NO:
            self.serial_no = str(res)
        elif command == CMD_METRICS:
            assert isinstance(res, dict)  # For Mypy
            self.serial_no = str(res["serial_number"])

        return res

    def read(self) -> bytes:
        res = self._conn.read_until(expected=b"\r")
        log.debug("%s < RAW %r", self._conn.port, res)
        self.reads += len(res)
        return res

    @retry
    def send(self, command: str) -> Result:
        self.write(command)
        return self.decode(command, self.read())

    def write(self, command: str) -> bool:
        full_command = f"{expand_command(command)}{compute_crc(command)}\r"
        log.debug("%s > SEND %r", self._conn.port, full_command)
        res = self._conn.write(serial.to_bytes(ord(c) for c in full_command))
        log.debug("%s > WRITTEN %r chars (%s)", self._conn.port, res, "OK" if res == len(full_command) else "ERROR")
        self.writes += res
        return res > 0
