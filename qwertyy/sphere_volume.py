import math

import math

pi = math.pi #Число Пи. Примерно, равное 3.141592653589793

def calculate_sphere_volume(r):
    try:
        a = 4/3*pi*r**3
    except TypeError:
        raise ValueError
    if a < 0:
        a = 'Радиус сферы не может быть отрицательным'
    return a