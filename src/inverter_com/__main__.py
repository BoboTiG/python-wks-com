"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
import sys


def main() -> int:
    if args := sys.argv[1:]:
        from inverter_com.helpers import test_command

        port = args[0]
        command = args[1]
        test_command(port, command)

    return 0


if __name__ == "__main__":  # pragma: nocover
    sys.exit(main())
