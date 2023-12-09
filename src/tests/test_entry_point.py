"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
from unittest.mock import patch

from inverter_com.__main__ import main


def test_no_args() -> None:
    with patch("sys.argv", []):
        assert main() == 0
