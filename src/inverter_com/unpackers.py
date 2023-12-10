"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-inverter-com
"""
from pydantic import BaseModel, Field, computed_field, field_validator

from inverter_com import constants, validators


class Flags(BaseModel):
    flags: str = Field(exclude=True, title="flags")

    @computed_field
    def silent_buzzer(self) -> bool:
        return self.flags.index("a") < self.flags.index("D")

    @computed_field
    def overload_function(self) -> bool:
        return self.flags.index("b") < self.flags.index("D")

    @computed_field
    def power_saving(self) -> bool:
        return self.flags.index("j") < self.flags.index("D")

    @computed_field
    def lcd_display_escape_timeout(self) -> bool:
        return self.flags.index("k") < self.flags.index("D")

    @computed_field
    def data_log_popup(self) -> bool:
        return self.flags.index("l") < self.flags.index("D")

    @computed_field
    def unknown(self) -> bool:
        # TODO: find out what is it for.
        return self.flags.index("n") < self.flags.index("D")

    @computed_field
    def overload_restart(self) -> bool:
        return self.flags.index("u") < self.flags.index("D")

    @computed_field
    def over_temperature_restart(self) -> bool:
        return self.flags.index("v") < self.flags.index("D")

    @computed_field
    def lcd_backlight(self) -> bool:
        return self.flags.index("x") < self.flags.index("D")

    @computed_field
    def alarm_on_primary_source_interrupt(self) -> bool:
        return self.flags.index("y") < self.flags.index("D")

    @computed_field
    def fault_code_recording(self) -> bool:
        return self.flags.index("z") < self.flags.index("D")


class Metrics(BaseModel):
    parallel_num: int
    serial_no: str
    work_mode: str
    fault_code: int
    grid_voltage: float
    grid_freq: float
    ac_output_voltage: float
    ac_output_freq: float
    ac_output_apparent_power: int
    ac_output_active_power: int
    load_percent: int
    battery_voltage: float
    battery_charging_current: int
    battery_capacity: int
    pv_input_voltage: float
    total_charging_current: int
    total_ac_output_apparent_power: int
    total_output_active_power: int
    total_ac_output_percent: int
    inverter_status: str
    output_mode: str
    charger_source_priority: str
    max_charger_current: int
    max_charger_range: int
    max_ac_charger_current: int
    pv_input_current_for_battery: int
    battery_discharge_current: int

    @computed_field
    def error(self) -> str:
        return self.get_error(self.fault_code)

    @computed_field
    def status_ac_charging(self) -> bool:
        return bool(self.get_status(self.inverter_status)["ac-charging"])

    @computed_field
    def status_battery(self) -> str:
        return str(self.get_status(self.inverter_status)["battery"])

    @computed_field
    def status_conf_changed(self) -> bool:
        return bool(self.get_status(self.inverter_status)["conf-changed"])

    @computed_field
    def status_line(self) -> str:
        return str(self.get_status(self.inverter_status)["line"])

    @computed_field
    def status_load(self) -> bool:
        return bool(self.get_status(self.inverter_status)["load"])

    @computed_field
    def status_ssc(self) -> str:
        return str(self.get_status(self.inverter_status)["ssc"])

    @computed_field
    def status_ssc_charging(self) -> bool:
        return bool(self.get_status(self.inverter_status)["ssc-charging"])

    @field_validator("charger_source_priority")
    def validate_charger_source_priority(cls, value: str) -> str:
        return validators.charger_source_priority(value)

    @field_validator("output_mode")
    def validate_output_mode(cls, value: str) -> str:
        return validators.output_mode(value)

    @field_validator("work_mode")
    def validate_work_mode(cls, value: str) -> str:
        return validators.work_mode(value)

    @staticmethod
    def get_error(errno: int) -> str:
        """
        >>> Metrics.get_error(0)
        'ok'
        >>> Metrics.get_error(80)
        'can-communication-failed'
        >>> Metrics.get_error(222)
        'error-222'
        """
        return constants.ERRORS.get(errno, f"error-{errno}")

    @staticmethod
    def get_status(status: str) -> dict[str, str | bool]:
        """
        >>> Metrics.get_status("00000000")
        {'ssc': 'lost', 'ac-charging': False, 'ssc-charging': False, 'battery': 'normal', 'line': 'ok', 'load': False, 'conf-changed': False}
        >>> Metrics.get_status("11100111")
        {'ssc': 'ok', 'ac-charging': True, 'ssc-charging': True, 'battery': 'normal', 'line': 'lost', 'load': True, 'conf-changed': True}
        >>> Metrics.get_status("00000000")["battery"]
        'normal'
        >>> Metrics.get_status("00001000")["battery"]
        'under'
        >>> Metrics.get_status("00002000")["battery"]
        'open'
        """  # noqa[E501]
        return {
            "ssc": "ok" if status[0] == "1" else "lost",
            "ac-charging": bool(int(status[1])),
            "ssc-charging": bool(int(status[2])),
            "battery": constants.BATTERY_STATUSES[status[3:5]],
            "line": "ok" if status[5] == "0" else "lost",
            "load": bool(int(status[6])),
            "conf-changed": bool(int(status[7])),
        }


class Ratings(BaseModel):
    grid_rating_voltage: float
    grid_rating_current: float
    ac_output_rating_voltage: float
    ac_output_rating_freq: float
    ac_output_rating_current: float
    ac_output_rating_apparent_power: int
    ac_output_rating_active_power: int
    battery_rating_voltage: float
    battery_recharge_voltage: float
    battery_under_voltage: float
    battery_bulk_voltage: float
    battery_float_voltage: float
    battery_type: str
    max_ac_charging_current: int
    max_charging_current: int
    input_voltage_range: str
    output_source_priority: str
    charger_source_priority: str
    parallel_max_num: int
    machine_type: str
    topology: str
    output_mode: str
    batter_redischarge_voltage: float
    pv_ok_condition_for_parallel: bool
    pv_power_balance: bool

    @field_validator("battery_type")
    def validate_battery_type(cls, value: str) -> str:
        return validators.battery_type(value)

    @field_validator("charger_source_priority")
    def validate_charger_source_priority(cls, value: str) -> str:
        return validators.charger_source_priority(value)

    @field_validator("input_voltage_range")
    def validate_input_voltage_range(cls, value: str) -> str:
        return validators.input_voltage_range(value)

    @field_validator("machine_type")
    def validate_machine_type(cls, value: str) -> str:
        return validators.machine_type(value)

    @field_validator("output_mode")
    def validate_output_mode(cls, value: str) -> str:
        return validators.output_mode(value)

    @field_validator("output_source_priority")
    def validate_output_source_priority(cls, value: str) -> str:
        return validators.output_source_priority(value)

    @field_validator("topology")
    def validate_topology(cls, value: str) -> str:
        return validators.topology(value)


class Settings(BaseModel):
    ac_output_voltage: float
    ac_output_freq: float
    max_ac_charging_current: int
    battery_under_voltage: float
    charging_float_voltage: float
    charging_bulk_voltage: float
    battery_default_recharge_voltage: float
    max_charging_current: int
    ac_input_voltage_range: int
    output_source_priority: str
    charger_source_priority: str
    battery_type: str
    silent_buzzer: bool
    power_saving: bool
    overload_restart: bool
    over_temperature_restart: bool
    lcd_backlight: bool
    alarm_on_primary_source_interrupt: bool
    fault_code_recording: bool
    overload_bypass: bool
    lcd_display_escape_timeout: int
    output_mode: str
    battery_redischarge_voltage: float
    pv_ok_condition_for_parallel: bool
    pv_power_balance: bool

    @field_validator("battery_type")
    def validate_battery_type(cls, value: str) -> str:
        return validators.battery_type(value)

    @field_validator("charger_source_priority")
    def validate_charger_source_priority(cls, value: str) -> str:
        return validators.charger_source_priority(value)

    @field_validator("output_mode")
    def validate_output_mode(cls, value: str) -> str:
        return validators.output_mode(value)

    @field_validator("output_source_priority")
    def validate_output_source_priority(cls, value: str) -> str:
        return validators.output_source_priority(value)


class Status(BaseModel):
    grid_voltage: float
    grid_freq: float
    ac_output_voltage: float
    ac_output_freq: float
    ac_output_apparent_power: int
    ac_output_active_power: int
    output_overload_percent: int
    bus_voltage: int
    battery_voltage: float
    battery_charging_current: int
    battery_capacity: int
    inverter_heat_sink_temperature: int
    pv_input_current_for_battery: int
    pv_input_voltage: float
    battery_voltage_from_scc: float
    battery_discharge_current: int
    status: str


class Warnings(BaseModel):
    warnings: str = Field(exclude=True, title="warnings")

    @computed_field
    def pv_loss(self) -> bool:
        return self.check(0)

    @computed_field
    def inverter_fault(self) -> bool:
        return self.check(1)

    @computed_field
    def bus_over(self) -> bool:
        return self.check(2)

    @computed_field
    def bus_under(self) -> bool:
        return self.check(3)

    @computed_field
    def bus_soft_fail(self) -> bool:
        return self.check(4)

    @computed_field
    def line_fail(self) -> bool:
        return self.check(5)

    @computed_field
    def opvshort(self) -> bool:
        return self.check(6)

    @computed_field
    def inverter_voltage_too_low(self) -> bool:
        return self.check(7)

    @computed_field
    def inverter_voltage_too_high(self) -> bool:
        return self.check(8)

    @computed_field
    def over_temperature(self) -> bool:
        return self.check(9)

    @computed_field
    def fan_locked(self) -> bool:
        return self.check(10)

    @computed_field
    def battery_voltage_high(self) -> bool:
        return self.check(11)

    @computed_field
    def battery_low_alarm(self) -> bool:
        return self.check(12)

    @computed_field
    def battery_under_shutdown(self) -> bool:
        return self.check(14)

    @computed_field
    def battery_derating(self) -> bool:
        return self.check(15)

    @computed_field
    def over_load(self) -> bool:
        return self.check(16)

    @computed_field
    def eeprom_fault(self) -> bool:
        return self.check(17)

    @computed_field
    def inverter_over_current(self) -> bool:
        return self.check(18)

    @computed_field
    def inverter_soft_fail(self) -> bool:
        return self.check(19)

    @computed_field
    def self_test_fail(self) -> bool:
        return self.check(20)

    @computed_field
    def op_dc_voltage_over(self) -> bool:
        return self.check(21)

    @computed_field
    def bat_open(self) -> bool:
        return self.check(22)

    @computed_field
    def current_sensor_fail(self) -> bool:
        return self.check(23)

    @computed_field
    def battery_week(self) -> bool:
        return self.check(31)

    def check(self, index: int) -> bool:
        return self.warnings[index] == "1"


class Time(BaseModel):
    time: str

    @field_validator("time")
    def validate_time(cls, value: str) -> str:
        return validators.time(value)


class TotalLoad(BaseModel):
    total_output_load_energy: int


class TotalPv(BaseModel):
    total_pv_generated_energy: int


# Unpack classes (going from a serial raw response to a managed Python object)
UNPACKERS: dict[str, BaseModel] = {
    constants.CMD_FLAGS: Flags,
    constants.CMD_METRICS: Metrics,
    constants.CMD_METRICS_1: Metrics,
    constants.CMD_METRICS_2: Metrics,
    constants.CMD_METRICS_3: Metrics,
    constants.CMD_METRICS_4: Metrics,
    constants.CMD_METRICS_5: Metrics,
    constants.CMD_METRICS_6: Metrics,
    constants.CMD_METRICS_7: Metrics,
    constants.CMD_METRICS_8: Metrics,
    constants.CMD_METRICS_9: Metrics,
    constants.CMD_RATINGS: Ratings,
    constants.CMD_SETTINGS: Settings,
    constants.CMD_STATUS: Status,
    constants.CMD_TIME: Time,
    constants.CMD_TOTAL_LOAD: TotalLoad,
    constants.CMD_TOTAL_PV: TotalPv,
    constants.CMD_WARNINGS: Warnings,
}


def unpack(command: str, seq: str) -> str | dict[str, str | int | float | bool]:
    """
    >>> # Command
    >>> unpack("QID", "96332309100452")
    '96332309100452'

    >>> # Alias (serial-no is an alias to the QID command)
    >>> unpack("serial-no", "96332309100452")
    '96332309100452'
    """
    if not (unpacker_cls := UNPACKERS.get(command)):
        return seq

    kwargs = {key: val for key, val in zip(unpacker_cls.model_fields, seq.split(" "))}
    metrics = unpacker_cls(**kwargs)
    return metrics.model_dump()
