"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-wks-com
"""
from datetime import datetime

from wks_com import constants


def battery_type(value: str) -> str:
    """
    >>> battery_type("0")
    'AGM'
    >>> battery_type("1")
    'Flooded'
    >>> battery_type("2")
    'User'
    >>> battery_type("3")
    'Pylontech'
    >>> battery_type("4")
    'Shinheung'
    >>> battery_type("5")
    'WECO'
    >>> battery_type("6")
    'Soltaro'
    >>> battery_type("7")
    'TBD'
    >>> battery_type("8")
    'LIb-protocol compatible'
    >>> battery_type("9")
    '3rd party Lithium'
    """
    return constants.BATTERY_TYPES[int(value)]


def charger_source_priority(value: str) -> str:
    """
    >>> charger_source_priority("0")
    'Utility first'
    >>> charger_source_priority("1")
    'Solar first'
    >>> charger_source_priority("2")
    'Solar + Utility'
    >>> charger_source_priority("3")
    'Solar only'
    """
    return constants.CHARGER_SOURCE_PRIORITIES[int(value)]


def error(value: str) -> str:
    """
    >>> error("00")
    'No fault'
    >>> error("80")
    'CAN communication failed'
    >>> error("222")
    'error 222'
    """
    return constants.ERRORS.get(value, f"error {value}")


def input_voltage_range(value: str) -> str:
    """
    >>> input_voltage_range("0")
    'appliance'
    >>> input_voltage_range("1")
    'ups'
    """
    return constants.INPUT_VOLTAGE_RANGES[int(value)]


def inverter_charge_status(value: str) -> str:
    """
    >>> inverter_charge_status("10")
    'no-charging'
    >>> inverter_charge_status("11")
    'bulk-stage'
    >>> inverter_charge_status("12")
    'absorb'
    >>> inverter_charge_status("13")
    'float'
    """
    return constants.INVERTER_CHARGE_STATUS[value]


def machine_type(value: str) -> str:
    """
    >>> machine_type("00")
    'Grid tie'
    >>> machine_type("01")
    'Off Grid'
    >>> machine_type("10")
    'Hybrid'
    """
    return constants.MACHINE_TYPES[value]


def output_mode(value: str) -> str:
    """
    >>> output_mode("00")
    'single machine'
    >>> output_mode("01")
    'parallel output'
    >>> output_mode("02")
    'Phase 1 of 3 phase output'
    >>> output_mode("03")
    'Phase 2 of 3 phase output'
    >>> output_mode("04")
    'Phase 3 of 3 phase output'
    >>> output_mode("05")
    'Phase 1 of 2 phase output'
    >>> output_mode("06")
    'Phase 2 of 2 phase output (120°)'
    >>> output_mode("07")
    'Phase 2 of 2 phase output (180°)'
    >>> output_mode("08")
    'Unknown'
    """
    return constants.OUTPUT_MODES[int(value)]


def output_source_priority(value: str) -> str:
    """
    >>> output_source_priority("0")
    'Utility Solar Battery'
    >>> output_source_priority("1")
    'Solar Utility Battery'
    >>> output_source_priority("2")
    'Solar Battery Utility'
    """
    return constants.OUTPUT_SOURCE_PRIORITIES[int(value)]


def parallel_mode(value: str) -> str:
    """
    >>> parallel_mode("0")
    'new'
    >>> parallel_mode("1")
    'slave'
    >>> parallel_mode("2")
    'master'
    """
    return constants.PARALLEL_MODE[int(value)]


def time(value: str) -> str:
    """
    >>> time("20231210204150")
    '2023-12-10 20:41:50'
    """
    return str(datetime.strptime(value, "%Y%m%d%H%M%S"))


def topology(value: str) -> str:
    """
    >>> topology("0")
    'transformerless'
    >>> topology("1")
    'transformer'
    """
    return constants.TOPOLOGIES[int(value)]


def work_mode(value: str) -> str:
    """
    >>> work_mode("B")
    'Battery Mode'
    >>> work_mode("D")
    'Shutdown Mode'
    >>> work_mode("F")
    'Fault Mode'
    >>> work_mode("H")
    'Power Saving Mode'
    >>> work_mode("L")
    'Line Mode'
    >>> work_mode("P")
    'Power On Mode'
    >>> work_mode("S")
    'Standby Mode'
    """
    return constants.WORK_MODES[value]
