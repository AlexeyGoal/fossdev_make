
from ndfl import calculate_ndfl

def test_ndfl_tier_1_basic():
    assert calculate_ndfl(2_000_000) == 260_000

def test_ndfl_tier2_basic():
    assert calculate_ndfl(4_000_00) == 552_000

def test_ndfl_tier3_basic():
    assert calculate_ndfl(10_000_000) == 1_602_000

def test_ndfl_tier4_basic():
    assert calculate_ndfl(30_000_000) == 5_402_000


def test_ndfl_tier5_basic():
    assert calculate_ndfl(60_000_000) == 11_602_000

