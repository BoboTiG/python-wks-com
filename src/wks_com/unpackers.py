"""
This is part of the inverter COM Python's module.
Source: https://github.com/BoboTiG/python-wks-com
"""

from pydantic import BaseModel, Field, computed_field, field_validator

from wks_com import constants, validators
from wks_com.types import Result


class QED(BaseModel):
    pv_generated_energy_for_day: int


class QEM(BaseModel):
    pv_generated_energy_for_month: int


class QET(BaseModel):
    pv_generated_energy_total: int


class QEY(BaseModel):
    pv_generated_energy_for_year: int


class QLD(BaseModel):
    output_load_energy_for_day: int


class QLM(BaseModel):
    output_load_energy_for_month: int


class QLT(BaseModel):
    output_load_energy_total: int


class QLY(BaseModel):
    output_load_energy_for_year: int


class QPGS0(BaseModel):
    parallel_instance_number: int
    serial_number: str
    work_mode: str
    fault_code: str
    ac_input_voltage: float
    ac_input_frequency: float
    ac_output_voltage: float
    ac_output_frequency: float
    ac_output_apparent_power: int
    ac_output_active_power: int
    load_percentage: int
    battery_voltage: float
    battery_charging_current: int
    battery_capacity: int
    pv1_input_voltage: float
    total_charging_current: int
    total_ac_output_apparent_power: int
    total_output_active_power: int
    total_ac_output_percentage: int
    inverter_status: str = Field(exclude=True)
    output_mode: str
    charger_source_priority: str
    max_charger_current: int
    max_charger_range: int
    max_ac_charger_current: int
    pv1_input_current: float  # Fix to align with QPIGS.pv1_input_current
    battery_discharge_current: int

    @computed_field
    def is_ac_charging(self) -> int:
        return int(self.inverter_status[1])

    @computed_field
    def is_battery_over_voltage(self) -> int:
        return int(self.inverter_status[3])

    @computed_field
    def is_battery_under_voltage(self) -> int:
        return int(self.inverter_status[4])

    @computed_field
    def is_configuration_changed(self) -> int:
        return int(self.inverter_status[7])

    @computed_field
    def is_line_lost(self) -> int:
        return int(self.inverter_status[5])

    @computed_field
    def is_load_on(self) -> int:
        return int(self.inverter_status[6])

    @computed_field
    def is_scc_charging(self) -> int:
        return int(self.inverter_status[2])

    @computed_field
    def is_scc_ok(self) -> int:
        return int(self.inverter_status[0])

    @field_validator("charger_source_priority")
    def validate_charger_source_priority(cls, value: str) -> str:
        return validators.charger_source_priority(value)

    @field_validator("fault_code")
    def validate_fault_code(cls, value: str) -> str:
        return validators.error(value)

    @field_validator("output_mode")
    def validate_output_mode(cls, value: str) -> str:
        return validators.output_mode(value)

    @field_validator("work_mode")
    def validate_work_mode(cls, value: str) -> str:
        return validators.work_mode(value)


class Q1(BaseModel):
    time_until_the_end_of_absorb_charging: int = Field(exclude=True)
    time_until_the_end_of_float_charging: int = Field(exclude=True)
    scc_ok: int = Field(exclude=True)
    allow_scc_on: int = Field(exclude=True)
    charge_average_current: int
    scc_temperature: int
    inverter_heat_sink_temperature: int
    battery_heat_sink_temperature: int
    transformer_temperature: int
    parallel_mode: str
    fan_lock_status: int = Field(exclude=True)
    gpio13: int = Field(exclude=True)
    fan_speed_percent: int
    scc_charge_power: int
    parallel_warning: str = Field(exclude=True)
    sync_frequency: float = Field(exclude=True)
    inverter_charge_status: str

    @field_validator("parallel_mode")
    def validate_parallel_mode(cls, value: str) -> str:
        return validators.parallel_mode(value)

    @field_validator("inverter_charge_status")
    def validate_inverter_charge_status(cls, value: str) -> str:
        return validators.inverter_charge_status(value)


class QPIGS(BaseModel):
    ac_input_voltage: float
    ac_input_frequency: float
    ac_output_voltage: float
    ac_output_frequency: float
    ac_output_apparent_power: int
    ac_output_active_power: int
    ac_load_percentage: int
    bus_voltage: int
    battery_voltage: float
    battery_charging_current: int
    battery_capacity: int
    inverter_heat_sink_temperature: int
    pv1_input_current: float
    pv1_input_voltage: float
    battery_voltage_from_scc: float
    battery_discharge_current: int
    device_status: str = Field(exclude=True)


class QPIRI(BaseModel):
    ac_input_rating_voltage: float
    ac_input_rating_current: float
    ac_output_rating_voltage: float
    ac_output_rating_frequency: float
    ac_output_rating_current: float
    ac_output_rating_apparent_power: int
    ac_output_rating_active_power: int
    battery_rating_voltage: float
    battery_recharge_voltage: float
    battery_under_voltage: float
    battery_bulk_charge_voltage: float
    battery_float_charge_voltage: float
    battery_type: str
    max_ac_charging_current: int
    max_charging_current: int
    input_voltage_range: str
    output_source_priority: str
    charger_source_priority: str
    max_parallel_units: int
    machine_type: str
    topology: str
    output_mode: str
    batter_redischarge_voltage: float
    pv_ok_condition: int
    pv_power_balance: int

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


class QPIWS(BaseModel):
    warnings: str = Field(exclude=True)

    @computed_field
    def pv_loss_warning(self) -> int:
        return self.check(0)

    @computed_field
    def inverter_fault(self) -> int:
        return self.check(1)

    @computed_field
    def bus_over_fault(self) -> int:
        return self.check(2)

    @computed_field
    def bus_under_fault(self) -> int:
        return self.check(3)

    @computed_field
    def bus_soft_fail_fault(self) -> int:
        return self.check(4)

    @computed_field
    def line_fail_warning(self) -> int:
        return self.check(5)

    @computed_field
    def opv_short_warning(self) -> int:
        return self.check(6)

    @computed_field
    def inverter_voltage_too_low_fault(self) -> int:
        return self.check(7)

    @computed_field
    def inverter_voltage_too_high_fault(self) -> int:
        return self.check(8)

    @computed_field
    def over_temperature_fault(self) -> int:
        return self.check(9)

    @computed_field
    def fan_locked_fault(self) -> int:
        return self.check(10)

    @computed_field
    def battery_voltage_high_fault(self) -> int:
        return self.check(11)

    @computed_field
    def battery_low_alarm_warning(self) -> int:
        return self.check(12)

    @computed_field
    def battery_under_shutdown_warning(self) -> int:
        return self.check(14)

    @computed_field
    def battery_derating_warning(self) -> int:
        return self.check(15)

    @computed_field
    def overload_fault(self) -> int:
        return self.check(16)

    @computed_field
    def eeprom_fault(self) -> int:
        return self.check(17)

    @computed_field
    def inverter_over_current_fault(self) -> int:
        return self.check(18)

    @computed_field
    def inverter_soft_fail_fault(self) -> int:
        return self.check(19)

    @computed_field
    def self_test_fail_fault(self) -> int:
        return self.check(20)

    @computed_field
    def op_dc_voltage_over_fault(self) -> int:
        return self.check(21)

    @computed_field
    def battery_open_fault(self) -> int:
        return self.check(22)

    @computed_field
    def current_sensor_fail_fault(self) -> int:
        return self.check(23)

    @computed_field
    def battery_short_fault(self) -> int:
        return self.check(31)

    def check(self, index: int) -> int:
        return int(self.warnings[index])


class QT(BaseModel):
    time: str

    @field_validator("time")
    def validate_time(cls, value: str) -> str:
        return validators.time(value)


# Unpack classes (going from a serial raw response to a managed Python object)
UNPACKERS: dict[str, BaseModel] = {
    constants.CMD_DAILY_LOAD: QLD,
    constants.CMD_DAILY_PV: QED,
    constants.CMD_METRICS: QPGS0,
    constants.CMD_MONTHLY_LOAD: QLM,
    constants.CMD_MONTHLY_PV: QEM,
    constants.CMD_Q1: Q1,
    constants.CMD_RATINGS: QPIRI,
    constants.CMD_STATUS: QPIGS,
    constants.CMD_TIME: QT,
    constants.CMD_TOTAL_LOAD: QLT,
    constants.CMD_TOTAL_PV: QET,
    constants.CMD_WARNINGS: QPIWS,
    constants.CMD_YEARLY_LOAD: QLY,
    constants.CMD_YEARLY_PV: QEY,
}


def unpack(command: str, seq: str) -> Result:
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

    kwargs = dict(zip(unpacker_cls.model_fields, seq.split(" "), strict=False))
    metrics = unpacker_cls(**kwargs)
    return metrics.model_dump()
