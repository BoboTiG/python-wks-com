"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
from argparse import ArgumentParser


def read() -> int:
    parser = ArgumentParser(prog="inverter-read")
    parser.add_argument("--port", default="/dev/ttyUSB0", help="serial port device")
    parser.add_argument("--debug", action="store_true", help="enable debug logging")
    parser.add_argument("command", nargs="+", help="command to send to the inverter")
    options = parser.parse_args()

    if options.command:
        from inverter_com.helpers import test_commands

        test_commands(options.port, *options.command, debug=options.debug)

    return 0
