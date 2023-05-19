class Car:
  marka = 'Wolzwagen'
  model = 'Comfort'
  year = 2020

  def get_attr(self):
    return (f'Марка: {Car.marka}, Модель: {Car.model}, Год выпуска: {Car.year}')

c = Car()
print(c.get_attr())