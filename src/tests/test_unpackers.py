"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
from inverter_com import constants
from inverter_com.unpackers import unpack


def test_unpack_metrics() -> None:
    seq = (
        "0 96332309100452 L 00 227.7 50.01 227.7 50.01 1252 1245 022 00.8 "
        "000 000 330.7 000 01252 01245 022 11102010 0 1 060 120 030 00 000"
    )
    res = unpack(constants.CMD_METRICS, seq)

    assert res == {
        "ac_output_active_power": 1245,
        "ac_output_apparent_power": 1252,
        "ac_output_freq": 50.01,
        "ac_output_voltage": 227.7,
        "battery_capacity": 0,
        "battery_charging_current": 0,
        "battery_discharge_current": 0,
        "battery_voltage": 0.8,
        "charger_source_priority": "solar-first",
        "error": "ok",
        "fault_code": 0,
        "grid_freq": 50.01,
        "grid_voltage": 227.7,
        "inverter_status": "11102010",
        "load_percent": 22,
        "max_ac_charger_current": 30,
        "max_charger_current": 60,
        "max_charger_range": 120,
        "output_mode": "single",
        "parallel_num": 0,
        "pv_input_current_for_battery": 0,
        "pv_input_voltage": 330.7,
        "serial_no": "96332309100452",
        "status_ac_charging": True,
        "status_battery": "open",
        "status_conf_changed": False,
        "status_line": "ok",
        "status_load": True,
        "status_ssc": "ok",
        "status_ssc_charging": True,
        "total_ac_output_apparent_power": 1252,
        "total_ac_output_percent": 22,
        "total_charging_current": 0,
        "total_output_active_power": 1245,
        "work_mode": "line",
    }


def test_unpack_ratings() -> None:
    seq = "230.0 24.3 230.0 50.0 24.3 5600 5600 48.0 46.0 42.0 56.4 54.0 3 030 060 0 2 1 9 00 0 0 54.0 0 1 000"
    res = unpack(constants.CMD_RATINGS, seq)

    assert res == {
        "ac_output_rating_active_power": 5600,
        "ac_output_rating_apparent_power": 5600,
        "ac_output_rating_current": 24.3,
        "ac_output_rating_freq": 50.0,
        "ac_output_rating_voltage": 230.0,
        "batter_redischarge_voltage": 54.0,
        "battery_bulk_voltage": 56.4,
        "battery_float_voltage": 54.0,
        "battery_rating_voltage": 48.0,
        "battery_recharge_voltage": 46.0,
        "battery_type": "pylontech",
        "battery_under_voltage": 42.0,
        "charger_source_priority": "solar-first",
        "grid_rating_current": 24.3,
        "grid_rating_voltage": 230.0,
        "input_voltage_range": "appliance",
        "machine_type": "grid-tie",
        "max_ac_charging_current": 30,
        "max_charging_current": 60,
        "output_mode": "single",
        "output_source_priority": "solar-battery-utility",
        "parallel_max_num": 9,
        "pv_ok_condition_for_parallel": False,
        "pv_power_balance": True,
        "topology": "transformerless",
    }


def test_unpack_status() -> None:
    seq = "231.0 50.0 231.0 50.0 0831 0816 014 363 00.70 001 001 0021 00.1 119.8 00.10 00001 00010110 01 01 00013 010"
    res = unpack(constants.CMD_STATUS, seq)

    assert res == {
        "ac_output_active_power": 816,
        "ac_output_apparent_power": 831,
        "ac_output_freq": 50.0,
        "ac_output_voltage": 231.0,
        "battery_capacity": 1,
        "battery_charging_current": 1,
        "battery_discharge_current": 1,
        "battery_voltage": 0.7,
        "battery_voltage_from_scc": 0.1,
        "bus_voltage": 363,
        "grid_freq": 50.0,
        "grid_voltage": 231.0,
        "inverter_heat_sink_temperature": 21,
        "output_overload_percent": 14,
        "pv_input_current": 0.1,
        "pv_input_voltage": 119.8,
        "status": "00010110",
    }


def test_unpack_daily_load() -> None:
    seq = "00007844"
    res = unpack(constants.CMD_DAILY_LOAD, seq)

    assert res == {"output_load_energy_for_day": 7844}


def test_unpack_daily_pv() -> None:
    seq = "00004820"
    res = unpack(constants.CMD_DAILY_PV, seq)

    assert res == {"pv_generated_energy_for_day": 4820}


def test_unpack_warnings() -> None:
    seq = "000000000000000000000010000000010000"
    res = unpack(constants.CMD_WARNINGS, seq)

    assert res == {
        "bat_open": True,
        "battery_derating": False,
        "battery_low_alarm": False,
        "battery_under_shutdown": False,
        "battery_voltage_high": False,
        "battery_week": True,
        "bus_over": False,
        "bus_soft_fail": False,
        "bus_under": False,
        "current_sensor_fail": False,
        "eeprom_fault": False,
        "fan_locked": False,
        "inverter_fault": False,
        "inverter_over_current": False,
        "inverter_soft_fail": False,
        "inverter_voltage_too_high": False,
        "inverter_voltage_too_low": False,
        "line_fail": False,
        "op_dc_voltage_over": False,
        "opvshort": False,
        "over_load": False,
        "over_temperature": False,
        "pv_loss": False,
        "self_test_fail": False,
    }
