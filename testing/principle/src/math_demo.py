def add(a,b):
    return a+b

def add_with_bug(a, b):
    return a*b

def tax_calculator_bugged(income):
    return income * 0.15

def tax_calculator(income):
    if income < 0:
        raise ValueError("Income cannot be negative")
    
    return int(income * 0.15 * 100) / 100