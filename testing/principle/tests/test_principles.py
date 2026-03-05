# import sys
# sys.path.append("../src")

from math_demo import add, add_with_bug, tax_calculator_bugged, tax_calculator

def test_addition():
    assert add(2,2) == 4
    print("assert passed")

def test_addition_with_bug():
    assert add_with_bug(2,3) == 6
    assert add_with_bug(2,2) == 4
    print("test bugged passed")

def test_addition_duplicate():
    assert add(6,7) == 6 + 7
    print("test duplicate addtion passed")

def test_addition_overkill():
    for i in range(0,2**32):
        for j in range(0,2**32):
            assert add(i,j) == i + j
            assert add(-i,j) == -i + j
            assert add(i,-j) == i - j

def test_addition_clusters():
    assert add(7,6) == 13
    assert add(0,6) == 6
    assert add(7,0) == 7
    assert add(10,-11) == -1
    assert add(-10, -11) == -21
    assert add(-5,0) == -5
    assert add(0,-2) == -2
    print("Test clusters passed")

def test_addition_commutative():
    assert add(10,4) == 14
    assert add(4,10) == 14
    print("Test commutative passed")


def test_cat_calculator_pesticide():
    assert tax_calculator_bugged(1000) == 150
    assert tax_calculator_bugged(100) == 15
    assert tax_calculator_bugged(10) == 1.5
    assert tax_calculator_bugged(1) == 0.15
    assert tax_calculator_bugged(234) == 35.1
    print("Test tax pesticide passed")
   # assert tax_calculator_bugged(2.34) == 0.35

def test_tax_calculator():
    assert tax_calculator(1000) == 150
    assert tax_calculator(100) == 15
    assert tax_calculator(10) == 1.5
    assert tax_calculator(1) == 0.15
    assert tax_calculator(234) == 35.1
    print("Test tax passed")
    #assert tax_calculator(2.34) == 0.35


if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()
    test_addition_clusters()
    test_addition_commutative()
    test_cat_calculator_pesticide()
    test_tax_calculator()
    # test_addition_overkill() can try