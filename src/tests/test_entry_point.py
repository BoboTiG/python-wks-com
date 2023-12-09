"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
from unittest.mock import patch

from inverter_com.__main__ import main


def test_command_from_func_args(port: str) -> None:
    with patch("inverter_com.inverter.Inverter.send") as mocked:
        mocked.return_value = {"foo": 42}
        assert main("cmd", "--port", port) == 0
        mocked.assert_called_with("cmd")


def test_command_from_func_sys_argv(port: str) -> None:
    with (
        patch("sys.argv", ["inverter-com", "cmd", "--port", port]),
        patch("inverter_com.inverter.Inverter.send") as mocked,
    ):
        mocked.return_value = {"foo": 42}
        assert main() == 0
        mocked.assert_called_with("cmd")
