import pytest
from src.embedded_functions import checksum

def test_checksum_valid():
    data = [1, 2, 3, 4]
    assert checksum(data) == 10

def test_checksum_overflow():
    data = [255, 255, 255]
    # Expect wrap-around since it's 8-bit
    assert checksum(data) == (255 + 255 + 255) & 0xFF
