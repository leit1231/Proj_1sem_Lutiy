from math import sqrt

def triangle_perimeter(a=7, b=2, c=8):
    '''Вычисление периметра треугольника'''
    p = a+b+c
    print(f'Периметр треугольника: {p}')

def triangle_area(a=7, b=2, c=8):
    '''Вычисление площади треугольника'''
    p = (a+b+c)/2
    s = round(sqrt(p*(p-a)*(p-b)*(p-c)), 1)
    print(f'Площадь треугольника: {s}')


