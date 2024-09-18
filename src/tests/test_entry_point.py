"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-wks-com
"""

import json
from unittest.mock import patch

import pytest

from wks_com import __main__

MOCKED_RETURN_VALUE = {"foo": 42}
FORMATTED_RETURN_VALUE = json.dumps(MOCKED_RETURN_VALUE, indent=4, sort_keys=True)


@pytest.mark.parametrize("debug", [True, False])
@pytest.mark.parametrize(
    "commands",
    [
        ["cmd"],
        ["cmd1", "cmd2"],
    ],
)
def test_read(
    commands: list[str], debug: bool, port: str, capsys: pytest.CaptureFixture, caplog: pytest.LogCaptureFixture
) -> None:
    full_cmd = ["wks-read", "--port", port, *commands]
    if debug:
        full_cmd.append("--debug")

    with patch("sys.argv", full_cmd), patch("wks_com.inverter.Inverter.send") as mocked:
        mocked.return_value = MOCKED_RETURN_VALUE
        assert __main__.read() == 0
        assert mocked.call_count == len(commands)
        for command in commands:
            mocked.assert_any_call(command)

    expected_output = "\n".join(f"{command}\n{FORMATTED_RETURN_VALUE}\n" for command in commands)
    assert capsys.readouterr().out.strip() == expected_output.strip()

    if debug:
        # As the logging level was lowered to DEBUG, we should see semothing here.
        # Maybe related to https://github.com/pytest-dev/pytest/issues/9393?
        assert not caplog.records
    else:
        assert not caplog.records
