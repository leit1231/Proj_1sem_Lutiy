#Дано целое число. Если оно является положительным, то прибавить к нему 1; если
#отрицательным, то вычесть из него 2; если нулевым, то заменить его на 10. Вывести
#полученное число
while True:     #обработка исключений
    try:
        a = int(input('Введите целое число:'))
        if a > 0:
            a = a+1
        elif a < 0:
            a = a-2
        else:
            a=10
        break
    except ValueError:
        print("Ошибка")
print(a)