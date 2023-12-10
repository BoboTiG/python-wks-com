"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
from datetime import datetime

from inverter_com import constants


def battery_type(value: str) -> str:
    """
    >>> battery_type("0")
    'agm'
    >>> battery_type("1")
    'flooded'
    >>> battery_type("2")
    'user'
    >>> battery_type("3")
    'pylon'
    >>> battery_type("4")
    'weco'
    >>> battery_type("5")
    'soltaro'
    >>> battery_type("6")
    'lib'
    >>> battery_type("7")
    'lic'
    """
    return constants.BATTERY_TYPES[int(value)]


def charger_source_priority(value: str) -> str:
    """
    >>> charger_source_priority("0")
    'utility-first'
    >>> charger_source_priority("1")
    'solar-first'
    >>> charger_source_priority("2")
    'solar-and-utility'
    >>> charger_source_priority("3")
    'solar-only'
    """
    return constants.CHARGER_SOURCE_PRIORITIES[int(value)]


def input_voltage_range(value: str) -> str:
    """
    >>> input_voltage_range("0")
    'appliance'
    >>> input_voltage_range("1")
    'ups'
    """
    return constants.INPUT_VOLTAGE_RANGES[int(value)]


def machine_type(value: str) -> str:
    """
    >>> machine_type("00")
    'grid-tie'
    >>> machine_type("01")
    'off-grid'
    >>> machine_type("10")
    'hybrid'
    >>> machine_type("11")
    'off-grid-with-2-trackers'
    >>> machine_type("20")
    'off-grid-with-3-trackers'
    """
    return constants.MACHINE_TYPES[value]


def output_mode(value: str) -> str:
    """
    >>> output_mode("00")
    'single'
    >>> output_mode("01")
    'parallel'
    >>> output_mode("02")
    'phase-1-of-3'
    >>> output_mode("03")
    'phase-2-of-3'
    >>> output_mode("04")
    'phase-3-of-3'
    >>> output_mode("05")
    'phase-1-of-2'
    >>> output_mode("06")
    'phase-2-of-2-120-deg'
    >>> output_mode("07")
    'phase-2-of-2-180-deg'
    """
    return constants.OUTPUT_MODES[int(value)]


def output_source_priority(value: str) -> str:
    """
    >>> output_source_priority("0")
    'utility-solar-bat'
    >>> output_source_priority("1")
    'solar-utility-bat'
    >>> output_source_priority("2")
    'solar-bat-utility'
    """
    return constants.OUTPUT_SOURCE_PRIORITIES[int(value)]


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
    'battery'
    >>> work_mode("F")
    'fault'
    >>> work_mode("H")
    'eco'
    >>> work_mode("L")
    'line'
    >>> work_mode("P")
    'power-on'
    >>> work_mode("S")
    'stand-by'
    """
    return constants.WORK_MODES[value]
