#Из предложенного текстового файла (text18-14.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив символы третей строки их числовыми
# кодами.
d = 0
for i in open('text18-14.txt', encoding='UTF-8'):
 print(i, end='')
 for j in i:
    if j == ' ':
        d += 1
print(end='\n')
print('Количество пробелов : ', d, end='\n')

f1 = open('text18-14.txt', 'r' ,encoding='UTF-8')
l = f1.readlines()
stroka = l[2]
cisla = [str(ord(x)) for x in stroka]
cisla.append('\n')
l[2] = ' '.join(cisla)
f1.close()
f2 = open('text18-14_2.txt', 'w')
f2.writelines(l)
f2.close()