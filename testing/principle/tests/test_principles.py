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

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()