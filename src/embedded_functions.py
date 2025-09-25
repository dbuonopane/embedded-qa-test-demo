import logging

#config logging
logging.basicConfig(
        filename="logs/test.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
)

def checksum(data: list[int]) -> int:
    """Simulates checksum calculation for embedded packet validation"""
    result = sum(data) & 0xFF
    logging.info(f"Checksum called with {data}, result={result}")
    return result, sum(data) & 0xFF  # simulate 8-bit checksum

def temperature_sensor(raw_value: int) -> float:
    """Convert raw ADC sensor reading into temperature (Celsius)"""
    base = (raw_value / 1023.0) * 100.0  # scale 0-100°C
    noise = random.uniform(-0.5, 0.5) #simulates sensor error
    temp  = base + noise
    logging.info(f"Temp sensor raw ={raw_value}, temp = {temp:.2f}"
    return temp

def voltage_monitor(voltage: float) -> bool:
    """Checks if voltage is within acceptable embedded system range"""
    return 3.0 <= voltage <= 4.2

def battery_voltage_trace() -> list[float]:
    """Sim battery voltage over time"""
    trace = [4.2, 4.0, 3.7, 3.5, 3.2, 3.0, 2.8]
    logging.info(f"Battery voltage trace {trace}")
    return trace

def system_operational(voltage: float) -> bool:
    """ system is ok if voltage >= 3.0V"""
    ok = voltage >= 3.0
    logging.info(f"Voltage={voltage}, operational={ok}")
    return ok
