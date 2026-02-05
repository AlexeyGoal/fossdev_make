def add(a,b):
    return a + b

def divide(a,b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    if isinstance(a,str) or isinstance(b,str):
        raise ValueError("Need arithmetic")
    return a/b






