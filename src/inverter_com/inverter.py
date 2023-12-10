"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
import logging
from dataclasses import dataclass, field

import serial

from inverter_com.constants import CMD_SERIAL_NO
from inverter_com.helpers import compute_crc, extract_response, retry
from inverter_com.types import Result
from inverter_com.unpackers import unpack

log = logging.getLogger(__name__)


@dataclass
class Inverter:
    port: str
    baudrate: int = field(default=2400, repr=False)
    bytesize: int = field(default=serial.EIGHTBITS, repr=False)
    parity: str = field(default=serial.PARITY_NONE, repr=False)
    reads: int = field(default=0, init=False)
    serial_no: str = field(init=False)
    stopbits: int = field(default=serial.STOPBITS_ONE, repr=False)
    writes: int = field(default=0, init=False)

    _conn: serial.Serial = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._conn = serial.Serial(
            baudrate=self.baudrate,
            bytesize=self.bytesize,
            parity=self.parity,
            port=self.port,
            stopbits=self.stopbits,
        )

        # Fetch the device serial number
        self.serial_no = str(self.send(CMD_SERIAL_NO))

    def read(self) -> bytes:
        res = self._conn.read_until(expected=b"\r")
        log.debug(f"{self._conn.port} < RAW {res!r}")
        self.reads += len(res)
        return res

    @retry
    def send(self, command: str) -> Result:
        self.write(command)
        res = unpack(command, extract_response(self.read()))
        log.debug(f"{self._conn.port} < DECODED {res!r}")
        return res

    def write(self, command: str) -> bool:
        full_command = command + compute_crc(command) + "\r"
        log.debug(f"{self._conn.port} > SEND {full_command!r}")
        res = self._conn.write(serial.to_bytes(ord(c) for c in full_command))
        log.debug(f"{self._conn.port} > WRITTEN {res!r} chars ({'OK' if res == len(full_command) else 'ERROR'})")
        self.writes += res
        return res > 0
