"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
from inverter_com.__main__ import main


def test_no_args() -> None:
    assert main() == 0
