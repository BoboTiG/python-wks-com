"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-wks-com
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
CMD_TOTAL_LOAD = "QLT"  # Query total output load energy, in W/h
CMD_TOTAL_PV = "QET"  # Query yearly output load energy, in W/h
CMD_WARNINGS = "QPIWS"  # Device warning status inquiry
CMD_YEARLY_LOAD = "QLY"  # Query yearly output load energy, in W/h
CMD_YEARLY_PV = "QEY"  # Query yearly PV generated energy, in W/h

# Used by unpackers
BATTERY_TYPES = [
    "AGM",
    "Flooded",
    "User",
    "Pylontech",
    "Shinheung",
    "WECO",
    "Soltaro",
    "TBD",
    "LIb-protocol compatible",
    "3rd party Lithium",
]
BATTERY_STATUSES = {
    "00": "normal",
    "01": "under",
    "02": "open",
}
CHARGER_SOURCE_PRIORITIES = [
    "Utility first",
    "Solar first",
    "Solar + Utility",
    "Solar only",
]
ERRORS = {
    "00": "No fault",
    "01": "Fan is locked",
    "02": "Over temperature",
    "03": "Battery voltage is too high",
    "04": "Battery voltage is too low",
    "05": "Output short circuited or Over temperature",
    "06": "Output voltage is too high",
    "07": "Over load time out",
    "08": "Bus voltage is too high",
    "09": "Bus soft start failed",
    "10": "PV over current",
    "11": "PV over voltage",
    "12": "DC over current",
    "13": "Battery discharge over current",
    "51": "Over current inverter",
    "52": "Bus voltage too low",
    "53": "Inverter soft start failed",
    "54": "Self-test failed",
    "55": "Over DC voltage on output of inverter",
    "56": "Battery connection is open",
    "57": "Current sensor failed",
    "58": "Output voltage is too low",
    "60": "Power feedback protection",
    "71": "Firmware version different",
    "72": "Current sharing fault",
    "80": "CAN communication failed",
    "81": "Parallel host line lost",
    "82": "Parallel synchronized signal lost",
    "83": "Parallel battery voltage detect different",
    "84": "AC input voltage or frequency detected different",
    "85": "AC output current unbalanced",
    "86": "AC output mode setting different",
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
    "00": "Grid tie",
    "01": "Off Grid",
    "10": "Hybrid",
}
OUTPUT_MODES = [
    "single machine",
    "parallel output",
    "Phase 1 of 3 phase output",
    "Phase 2 of 3 phase output",
    "Phase 3 of 3 phase output",
    "Phase 1 of 2 phase output",
    "Phase 2 of 2 phase output (120°)",
    "Phase 2 of 2 phase output (180°)",
    "Unknown",
]
OUTPUT_SOURCE_PRIORITIES = [
    "Utility Solar Battery",
    "Solar Utility Battery",
    "Solar Battery Utility",
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
    "P": "Power On Mode",
    "S": "Standby Mode",
    "L": "Line Mode",
    "B": "Battery Mode",
    "F": "Fault Mode",
    "H": "Power Saving Mode",
    "D": "Shutdown Mode",
}
