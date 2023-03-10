from math import pi

defolt_radius = 5

def circle_perimeter(radius = defolt_radius):
    '''Вычисление длины окружности'''
    c = 2 * pi * radius
    print(f"Длина окружности: {round(c, 1)}")


def circle_area(radius = defolt_radius):
    '''Вычисление площади круга'''
    c = pi*radius**2
    print(f"Площадь круга: {round(c, 1)}")

