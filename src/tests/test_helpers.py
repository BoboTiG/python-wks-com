import pytest
from freezegun import freeze_time

from wks_com import constants, helpers


@pytest.mark.parametrize(
    ("command", "format_expected"),
    [
        (constants.CMD_DAILY_LOAD, "yyyymmdd"),
        (constants.CMD_DAILY_PV, "yyyymmdd"),
        (constants.CMD_MONTHLY_LOAD, "yyyymm"),
        (constants.CMD_MONTHLY_PV, "yyyymm"),
        (constants.CMD_YEARLY_LOAD, "yyyy"),
        (constants.CMD_YEARLY_PV, "yyyy"),
    ],
)
@pytest.mark.parametrize(
    "today",
    [
        "2023-12-10",  # No padding
        "2024-09-07",  # Padding required (see issue #2)
    ],
)
def test_expand_command_date_format(today: str, command: str, format_expected: str) -> None:
    with freeze_time(today):
        assert len(helpers.expand_command(command)) == len(f"{command}{format_expected}")
