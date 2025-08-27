def checksum(data: list[int]) -> int:
    """Simulates checksum calculation for embedded packet validation"""
    return sum(data) & 0xFF  # simulate 8-bit checksum

def temperature_sensor(raw_value: int) -> float:
    """Convert raw ADC sensor reading into temperature (Celsius)"""
    return (raw_value / 1023.0) * 100.0  # scale 0-100°C

def voltage_monitor(voltage: float) -> bool:
    """Checks if voltage is within acceptable embedded system range"""
    return 3.0 <= voltage <= 4.2
