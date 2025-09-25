import pytest
from src.embedded_functions import temperature_sensor, voltage_monitor

def test_temperature_conversion():
    raw = 512  # mid-scale ADC value
    for i in range(20): # 20 noise samples
        temp = temperature_sensor(raw)
        assert 49.0 <= temp <= 51.0  # +- 1.5 celcius tolerance

def test_voltage_monitor_in_range():
    assert voltage_monitor(3.7) is True

def test_voltage_monitor_out_of_range():
    assert voltage_monitor(2.5) is False
    assert voltage_monitor(4.5) is False

def test_battery_voltage_dropout():
    for v in battery_voltage_trace():
        if v >= 3.0:
            assert system_operational(v) is True
        else:
            assert system_operational(v) is False

