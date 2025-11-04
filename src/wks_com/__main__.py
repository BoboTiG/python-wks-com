"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-wks-com
"""

from argparse import ArgumentParser

from wks_com import constants


def read() -> int:
    parser = ArgumentParser(prog="wks-read")
    parser.add_argument("--port", default=constants.DEFAULT_PORT, help="serial port device")
    parser.add_argument("--debug", action="store_true", help="enable debug logging")
    parser.add_argument("command", nargs="+", help="command to send to the inverter")
    options = parser.parse_args()

    if options.command:
        from wks_com.helpers import test_commands  # noqa: PLC0415

        test_commands(options.port, *options.command, debug=options.debug)

    return 0
