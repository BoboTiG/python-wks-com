"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
# Commands
CMD_FLAGS = "QFLAG"  # Device flag status inquiry
CMD_METRICS = "QPGS0"  # Parallel information inquiry
CMD_METRICS_1 = "QPGS1"
CMD_METRICS_2 = "QPGS2"
CMD_METRICS_3 = "QPGS3"
CMD_METRICS_4 = "QPGS4"
CMD_METRICS_5 = "QPGS5"
CMD_METRICS_6 = "QPGS6"
CMD_METRICS_7 = "QPGS7"
CMD_METRICS_8 = "QPGS8"
CMD_METRICS_9 = "QPGS9"
CMD_RATINGS = "QPIRI"  # Device rating information inquiry
CMD_SERIAL_NO = "QID"  # Device serial number inquiry
CMD_SETTINGS = "QDI"  # Default setting value information inquiry
CMD_STATUS = "QPIGS"  # Device general status parameters inquiry
CMD_TIME = "QT"  # Time inquiry
CMD_TOTAL_LOAD = "QLT"  # Query total output load energy
CMD_TOTAL_PV = "QET"  # Query total PV generated energy
CMD_WARNINGS = "QPIWS"  # Device warning status inquiry

# Used by unpackers
BATTERY_TYPES = [
    "agm",
    "flooded",
    "user",
    "pylon",
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
    "utility-solar-bat",
    "solar-utility-bat",
    "solar-bat-utility",
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
