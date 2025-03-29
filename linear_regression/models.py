import re
# This script is going to describe the general trend given two points on a line (in other words, m or slope)
def m(x_1: float, y_1: float, x_2: float, y_2: float):
    num = y_2 - y_1
    denom = x_2 - x_1
    return num / denom

def point_slope(m: float, x: float, y: float):
    #y^1 or f(x) - y = m(x - x^1)
    m_x = m * x
    global left
    global right
    if y >= 0:
        left = f"y - {y}"
    if y < 0:
        sign_differential = y * -1
        left = f"y + {sign_differential}"
    if m_x >= 0: 
        right = f"{m}x + {m_x}"
    if m_x < 0:
        right = f"{m}x{m_x}"
    return f"{left} = {right}"




def lin_regres(ps):
    #print(ps.split('y -'))
    find_float_values = re.findall("[-+]?[0-9]*\.?[0-9]+", ps)
    float_values = []

    for find_float_value in find_float_values:
        float_values.append(float(find_float_value))
    
    if "y -" in ps:
        combine = (float_values[0]) + float_values[2]
    if "y +" in ps:
        combine = (float_values[0] * -1) + float_values[2]
    if combine >= 0:
        return f"y = {float_values[1]}x + {combine}"
    if combine < 0:
        return f"y = {float_values[1]}x{combine}"


        


    #return float_values, combine





    
    


