# Создайте базовый класс "Форма" со свойствами "цвет" и "тип". От этого класса
# унаследуйте класс "Круг" и добавьте в него свойство "радиус". Определите методы
# вычисления площади и периметра
import math
class Form:
  def __init__(self, color: str, type_form: str):
    self.__color = color
    self.__type_form = type_form


class Circle(Form):
  def __init__(self, color, type_form, radius):
    super().__init__(color, type_form)
    self.radius = radius

  def pr_cr(self):
    if isinstance(self.radius, int):
      return round(2 * math.pi * self.radius)
    else:
      raise TypeError('Radius not int')

  def pl_cr(self):
    if isinstance(self.radius, int):
      return round(math.pi * self.radius ** 2)
    else:
      raise TypeError('Radius not int')


cr = Circle('red', 'circle', 5)
print(cr.pl_cr())
print(cr.pr_cr())