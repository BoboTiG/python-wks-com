"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-wks-com
"""
from wks_com import constants, unpackers
from wks_com.unpackers import unpack


def check_types(unpacker: object, res: dict) -> None:
    for field, metadata in unpacker.model_fields.items():
        if not metadata.exclude:
            assert isinstance(res[field], metadata.annotation)


def test_Q1() -> None:
    seq = (
        "00001 00001 00 00 00 024 025 019 024 02 00 000 0033 0000"
        " 0000 00.00 11 0 060 030 080 030 58.40 000 120 0 0000"
    )
    res = unpack(constants.CMD_Q1, seq)

    assert res == {
        "battery_heat_sink_temperature": 19,
        "charge_average_current": 0,
        "fan_speed_percent": 33,
        "inverter_charge_status": "bulk-stage",
        "inverter_heat_sink_temperature": 25,
        "parallel_mode": "master",
        "scc_charge_power": 0,
        "scc_temperature": 24,
        "transformer_temperature": 24,
    }
    check_types(unpackers.Q1, res)


def test_QED() -> None:
    seq = "00004820"
    res = unpack(constants.CMD_DAILY_PV, seq)

    assert res == {"pv_generated_energy_for_day": 4820}
    check_types(unpackers.QED, res)


def test_QEM() -> None:
    seq = "00004820"
    res = unpack(constants.CMD_MONTHLY_PV, seq)

    assert res == {"pv_generated_energy_for_month": 4820}
    check_types(unpackers.QEM, res)


def test_QET() -> None:
    seq = "00004820"
    res = unpack(constants.CMD_TOTAL_PV, seq)

    assert res == {"pv_generated_energy_total": 4820}
    check_types(unpackers.QET, res)


def test_QEY() -> None:
    seq = "00004820"
    res = unpack(constants.CMD_YEARLY_PV, seq)

    assert res == {"pv_generated_energy_for_year": 4820}
    check_types(unpackers.QEY, res)


def test_QLD() -> None:
    seq = "00007844"
    res = unpack(constants.CMD_DAILY_LOAD, seq)

    assert res == {"output_load_energy_for_day": 7844}
    check_types(unpackers.QLD, res)


def test_QLM() -> None:
    seq = "00007844"
    res = unpack(constants.CMD_MONTHLY_LOAD, seq)

    assert res == {"output_load_energy_for_month": 7844}
    check_types(unpackers.QLM, res)


def test_QLT() -> None:
    seq = "00007844"
    res = unpack(constants.CMD_TOTAL_LOAD, seq)

    assert res == {"output_load_energy_total": 7844}
    check_types(unpackers.QLT, res)


def test_QLY() -> None:
    seq = "00007844"
    res = unpack(constants.CMD_YEARLY_LOAD, seq)

    assert res == {"output_load_energy_for_year": 7844}
    check_types(unpackers.QLY, res)


def test_QPGS0() -> None:
    seq = (
        "0 96332309100452 L 00 227.7 50.01 227.7 50.01 1252 1245 022 00.8 "
        "000 000 330.7 000 01252 01245 022 11102010 0 1 060 120 030 00 000"
    )
    res = unpack(constants.CMD_METRICS, seq)

    assert res == {
        "ac_input_frequency": 50.01,
        "ac_input_voltage": 227.7,
        "ac_output_active_power": 1245,
        "ac_output_apparent_power": 1252,
        "ac_output_frequency": 50.01,
        "ac_output_voltage": 227.7,
        "battery_capacity": 0,
        "battery_charging_current": 0,
        "battery_discharge_current": 0,
        "battery_voltage": 0.8,
        "charger_source_priority": "Solar first",
        "fault_code": "No fault",
        "is_ac_charging": 1,
        "is_battery_over_voltage": 0,
        "is_battery_under_voltage": 2,
        "is_configuration_changed": 0,
        "is_line_lost": 0,
        "is_load_on": 1,
        "is_scc_charging": 1,
        "is_scc_ok": 1,
        "load_percentage": 22,
        "max_ac_charger_current": 30,
        "max_charger_current": 60,
        "max_charger_range": 120,
        "output_mode": "single machine",
        "parallel_instance_number": 0,
        "pv1_input_current": 0.0,
        "pv1_input_voltage": 330.7,
        "serial_number": "96332309100452",
        "total_ac_output_apparent_power": 1252,
        "total_ac_output_percentage": 22,
        "total_charging_current": 0,
        "total_output_active_power": 1245,
        "work_mode": "Line Mode",
    }
    check_types(unpackers.QPGS0, res)


def test_QPIGS() -> None:
    seq = "231.0 50.0 231.0 50.0 0831 0816 014 363 00.70 001 001 0021 00.1 119.8 00.10 00001 00010110 01 01 00013 010"
    res = unpack(constants.CMD_STATUS, seq)

    assert res == {
        "ac_input_frequency": 50.0,
        "ac_input_voltage": 231.0,
        "ac_load_percentage": 14,
        "ac_output_active_power": 816,
        "ac_output_apparent_power": 831,
        "ac_output_frequency": 50.0,
        "ac_output_voltage": 231.0,
        "battery_capacity": 1,
        "battery_charging_current": 1,
        "battery_discharge_current": 1,
        "battery_voltage": 0.7,
        "battery_voltage_from_scc": 0.1,
        "bus_voltage": 363,
        "inverter_heat_sink_temperature": 21,
        "pv1_input_current": 0.1,
        "pv1_input_voltage": 119.8,
    }
    check_types(unpackers.QPIGS, res)


def test_QPIRI() -> None:
    seq = "230.0 24.3 230.0 50.0 24.3 5600 5600 48.0 46.0 42.0 56.4 54.0 3 030 060 0 2 1 9 00 0 0 54.0 0 1 000"
    res = unpack(constants.CMD_RATINGS, seq)

    assert res == {
        "ac_input_rating_current": 24.3,
        "ac_input_rating_voltage": 230.0,
        "ac_output_rating_active_power": 5600,
        "ac_output_rating_apparent_power": 5600,
        "ac_output_rating_current": 24.3,
        "ac_output_rating_frequency": 50.0,
        "ac_output_rating_voltage": 230.0,
        "batter_redischarge_voltage": 54.0,
        "battery_bulk_charge_voltage": 56.4,
        "battery_float_charge_voltage": 54.0,
        "battery_rating_voltage": 48.0,
        "battery_recharge_voltage": 46.0,
        "battery_type": "Pylontech",
        "battery_under_voltage": 42.0,
        "charger_source_priority": "Solar first",
        "input_voltage_range": "appliance",
        "machine_type": "Grid tie",
        "max_ac_charging_current": 30,
        "max_charging_current": 60,
        "max_parallel_units": 9,
        "output_mode": "single machine",
        "output_source_priority": "Solar Battery Utility",
        "pv_ok_condition": 0,
        "pv_power_balance": 1,
        "topology": "transformerless",
    }
    check_types(unpackers.QPIRI, res)


def test_QPIWS() -> None:
    seq = "000000000000000000000010000000010000"
    res = unpack(constants.CMD_WARNINGS, seq)

    assert res == {
        "battery_open_fault": 1,
        "battery_derating_warning": 0,
        "battery_low_alarm_warning": 0,
        "battery_under_shutdown_warning": 0,
        "battery_voltage_high_fault": 0,
        "battery_short_fault": 1,
        "bus_over_fault": 0,
        "bus_soft_fail_fault": 0,
        "bus_under_fault": 0,
        "current_sensor_fail_fault": 0,
        "eeprom_fault": 0,
        "fan_locked_fault": 0,
        "inverter_fault": 0,
        "inverter_over_current_fault": 0,
        "inverter_soft_fail_fault": 0,
        "inverter_voltage_too_high_fault": 0,
        "inverter_voltage_too_low_fault": 0,
        "line_fail_warning": 0,
        "op_dc_voltage_over_fault": 0,
        "opv_short_warning": 0,
        "overload_fault": 0,
        "over_temperature_fault": 0,
        "pv_loss_warning": 0,
        "self_test_fail_fault": 0,
    }
    check_types(unpackers.QPIWS, res)


def test_QT() -> None:
    seq = "20231210204150"
    res = unpack(constants.CMD_TIME, seq)

    assert res == {"time": "2023-12-10 20:41:50"}
    check_types(unpackers.QT, res)
