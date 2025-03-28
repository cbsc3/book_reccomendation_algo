#This script is going to describe the general trend given two points on a line (in other words, m or slope)
def m(x_1: float, y_1: float, x_2: float, y_2: float):
    num = y_2 - y_1
    denom = x_2 - x_1
    return num / denom

def lin_regres(m: float, x: float, y: float):
    #y^1 or f(x) - y = m(x - x^1)
    m_x = m * x
    if y >= 0:
        left = f"y - {y}"
    if y < 0:
        sign_differential = y * -1
        left = f"y + {sign_differential}"
    

    #return f"y - {y} = {m}(x - {x})""
    return left

print(lin_regres(5.0, 2.0, 1.0))