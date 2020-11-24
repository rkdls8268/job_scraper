# plus, minus, times, division, negation, power, remainder

def plus(a, b):
    return int(a)+int(b)

def plus2(a, b):
    if type(b) is str or type(a) is str:
        return None
    else:
        return a + b

print(plus2(3, "5"))

def minus(a, b):
    return int(a)-int(b)

def times(a, b):
    return int(a)*int(b)

def division(a, b):
    return int(a)/int(b)

def negation(a):
    return -int(a)

def power(a, b):
    return pow(int(a), int(b))

def remainder(a, b):
    return int(a) % int(b)

plus_result = plus(10, 3)
minus_result = minus(10, 3)
times_result = times(10, 3)
division_result = division(10, 3)
negation_result = negation(10)
power_result = power(10, 3)
remainder_result = remainder(10, 3)

print(plus_result, minus_result, times_result, division_result, negation_result, power_result, remainder_result)