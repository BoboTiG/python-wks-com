"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
import sys
from argparse import ArgumentParser


def main(*args: str) -> int:
    parser = ArgumentParser(prog="inverter-com")
    parser.add_argument("--port", default="/dev/ttyUSB0", help="serial port device")
    parser.add_argument("--debug", action="store_true", help="enable debug logging")
    parser.add_argument("command", help="the command to send to the inverter")
    options = parser.parse_args(args or None)

    if options.command:
        from inverter_com.helpers import test_command

        test_command(options.port, options.command, debug=options.debug)

    return 0


if __name__ == "__main__":  # pragma: nocover
    sys.exit(main())
