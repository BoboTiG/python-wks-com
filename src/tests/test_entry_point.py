"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
from unittest.mock import patch

from inverter_com import __main__


def test_read_single_command(port: str) -> None:
    with (
        patch("sys.argv", ["inverter-read", "cmd", "--port", port]),
        patch("inverter_com.inverter.Inverter.send") as mocked,
    ):
        mocked.return_value = {"foo": 42}
        assert __main__.read() == 0
        assert mocked.call_count == 2
        mocked.assert_called_with("cmd")


def test_read_multiple_commands(port: str) -> None:
    with (
        patch("sys.argv", ["inverter-read", "cmd1", "cmd2", "--port", port]),
        patch("inverter_com.inverter.Inverter.send") as mocked,
    ):
        mocked.return_value = {"foo": 42}
        assert __main__.read() == 0
        assert mocked.call_count == 3
        mocked.assert_any_call("cmd1")
        mocked.assert_any_call("cmd2")
