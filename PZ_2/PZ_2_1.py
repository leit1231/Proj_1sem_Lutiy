# Вывод первой цифры трёхзначного числа
while True: #обработка исключений
    try:
        a = int(input("Введите целое трёхзначное число:")) #Ввод трёхзначного числа
        print(a // 100)
        break
    except ValueError:
        print("Что-то пошло не так")
print("hello world")
