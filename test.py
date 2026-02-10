from script import add, divide

def test_sum():
    a = 1
    b = 2
    result = 3
    assert add(a,b) == result

def test_divide():
    a = 4
    b = 2
    assert divide(a,b) == 2
def test_division_prohibited():
    try:
        divide("A","B")
#sdfas
test_sum()
test_divide()
