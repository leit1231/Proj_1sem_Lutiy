# Дана строка. Подсчитать количество содержащихся в ней прописных латинских
# букв.
while True:     #обработка исключений
    try:
        string = 'qwertyuiopasdfghjklzxcvbnm'   #все латинские прописные буквы
        a = input('Введите текст: ')
        n = 0
        for i in a: #проверка строки на наличие прописных латинских букв
            if i in string:
                n+=1
        print(n)
        break
    except:
        print("Ошибка!")