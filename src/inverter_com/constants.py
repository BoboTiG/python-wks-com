"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
# Timezone to tweak some commands output
TIMEZONE = "Europe/Paris"

# Commands
CMD_DAILY_LOAD = "QLD"  # Query daily output load energy, in W/h
CMD_DAILY_PV = "QED"  # Query daily PV generated energy, in W/h
CMD_METRICS = "QPGS0"  # Parallel information inquiry
CMD_MODEL = "QMN"  # Query model name
CMD_MONTHLY_LOAD = "QLM"  # Query monthly output load energy, in W/h
CMD_MONTHLY_PV = "QEM"  # Query monthly PV generated energy, in W/h
CMD_Q1 = "Q1"  # "The Q1 command", thanks to the documentation ...
CMD_RATINGS = "QPIRI"  # Device rating information inquiry
CMD_SERIAL_NO = "QID"  # Device serial number inquiry
CMD_STATUS = "QPIGS"  # Device general status parameters inquiry
CMD_TIME = "QT"  # Time inquiry
CMD_WARNINGS = "QPIWS"  # Device warning status inquiry
CMD_YEARLY_LOAD = "QLY"  # Query yearly output load energy, in W/h
CMD_YEARLY_PV = "QEY"  # Query yearly PV generated energy, in W/h

# Used by unpackers
BATTERY_TYPES = [
    "agm",
    "flooded",
    "user",
    "pylontech",
    "weco",
    "soltaro",
    "lib",
    "lic",
]
BATTERY_STATUSES = {
    "00": "normal",
    "01": "under",
    "02": "open",
}
CHARGER_SOURCE_PRIORITIES = [
    "utility-first",
    "solar-first",
    "solar-and-utility",
    "solar-only",
]
ERRORS = {
    0: "ok",
    1: "fan-locked",
    2: "temperature-too-high",
    3: "battery-voltage-too-high",
    4: "battery-voltage-too-low",
    5: "output-short-circuited-or-temperature-too-high",
    6: "output-voltage-too-high",
    7: "overload-timeout",
    8: "bus-voltage-too-high",
    9: "bus-soft-start-failed",
    11: "main-relay-failed",
    51: "over-curent-inverter",
    52: "bus-soft-start-failed",
    53: "inverter-soft-start-failed",
    54: "self-test-failed",
    55: "over-dv-voltage-on-output-inverter",
    56: "battery-connection-open",
    57: "current-sensor-failed",
    58: "output-voltage-too-low",
    60: "inverter-negative-power",
    71: "parallel-version-different",
    72: "output-circuit-failed",
    80: "can-communication-failed",
    81: "parallel-host-line-lost",
    82: "parallel-synchronized-signal-host",
    83: "parallel-battery-voltage-detect-different",
    84: "parallel-line-voltage-or-frequency-detect-different",
    85: "parallel-line-input-current-unbalanced",
    86: "parallel-output-setting different",
}
INPUT_VOLTAGE_RANGES = [
    "appliance",
    "ups",
]
INVERTER_CHARGE_STATUS = {
    "10": "no-charging",
    "11": "bulk-stage",
    "12": "absorb",
    "13": "float",
}
MACHINE_TYPES = {
    "00": "grid-tie",
    "01": "off-grid",
    "10": "hybrid",
    "11": "off-grid-with-2-trackers",
    "20": "off-grid-with-3-trackers",
}
OUTPUT_MODES = [
    "single",
    "parallel",
    "phase-1-of-3",
    "phase-2-of-3",
    "phase-3-of-3",
    "phase-1-of-2",
    "phase-2-of-2-120-deg",
    "phase-2-of-2-180-deg",
]
OUTPUT_SOURCE_PRIORITIES = [
    "utility-solar-battery",
    "solar-utility-battery",
    "solar-battery-utility",
]
PARALLEL_MODE = [
    "new",
    "slave",
    "master",
]
TOPOLOGIES = [
    "transformerless",
    "transformer",
]
WORK_MODES = {
    "B": "battery",
    "F": "fault",
    "H": "eco",
    "L": "line",
    "P": "power-on",
    "S": "stand-by",
}
