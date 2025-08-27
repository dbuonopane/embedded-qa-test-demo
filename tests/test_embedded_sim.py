import pytest
from src.embedded_functions import temperature_sensor, voltage_monitor

def test_temperature_conversion():
    raw = 512  # mid-scale ADC value
    temp = temperature_sensor(raw)
    assert 49.0 <= temp <= 51.0  # allow tolerance

def test_voltage_monitor_in_range():
    assert voltage_monitor(3.7) is True

def test_voltage_monitor_out_of_range():
    assert voltage_monitor(2.5) is False
    assert voltage_monitor(4.5) is False
