# import sys
# sys.path.append("../src")

from math_demo import add, add_with_bug

def test_addition():
    assert add(2,2) == 4
    print("assert passed")

def test_addition_with_bug():
    assert add_with_bug(2,3) == 5
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

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()
    # test_addition_overkill() can try