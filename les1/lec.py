# print ("Hello world")

# #value = None
# #a = 123
# #b = 1.23
# #print(type(a))
# print(b)
# s = "Hello \nWorld" # \n - новая строка 
# print (s)

# print (a , '-', b)
# print ('{} - {} '.format(a, b))
# print (f'{a} - {b}')

# f = True

#                   Списки

# list = [1, 2, 3]
# col = ['hello', 1, '2']
# print (col)

#               Ввод и вывод данных
# print input

# print ('Введите а')
# a = float(input())
# print ('Введите b')
# b = int(input ()) # int
# print (a , '+', b, '=', a+b) # a + b= ab, пожтому нужет int- при целых значениях, float - при дробных
# print (a , '-', b)
# print ('{} - {} '.format(a, b))
# print (f'{a} - {b}')


#       Аифметика 
# + - * / 
# // - делить без остатка 
# % - остаток от деления
# ** - возведение в степень
# 1.3 * 3 = 3.900000...4 -чтобы такого не было - round(a*b,3) - 3 количество цифр после запятой

# a= 1.3
# b= 3
# c= a * b
# print(c)

# a = 3
# a = a + 5 # омжн написать a += 5, также *= , /= и тд

#           Логические операции
# < > == ...
# not , and,  or - не путать с  &, |, ^ 
# is, is not, in, not in
# gen

# f = [1, 2, 3, 4]
# print (f)
#print (not 2 in f) # нет 2 в списке f - лож

# is_odd = f[2] % 2 # остаток от деления на 2 число в списке f то есть 3  будет 1- 3 / 2 = 1 ост 1
# is_odd = not f[2] % 2 # False
# print (is_odd)

#               IF IF-ELSE
# if, if- else, elif

# a = int(input())
# b = int(input())
# if a > b:
#     print (a)
# else: 
#     print (b)

#           цикл
# while ELSE  for  in

# orig = 23
# inverted = 0
# while orig != 0:
#     inverted = inverted * 10 + (orig % 10)
#     orig //= 10
# else:
#     print("")
# print (inverted)

# list = [1,2,3,4,5]
# r = range (10) # перечисяет от 0 до 9
# for i in range (1, 10, 2): # range - перечисляет от 1 до 9 с шагом 2
#     print(i)

#           Строки

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'

# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.lower()) # съешь ещё этих мягких французских булок
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

# #               СРЕЗЫ
# text = 'съешь ещё этих мягких французских булок'
#  print(text[0]) # c
#  print(text[1]) # ъ
#  print(text[len(text)-1]) # к
#  print(text[-5]) # б
#  print(text[:]) # съешь ещё этих мягких французских булок
#  print(text[:2]) # съ

#  #      
#  print(text[len(text)-2:]) # ок
#  print(text[2:9]) # ешь ещё
#  print(text[6:-18]) # ещё этих мягких
#  print(text[0:len(text):6]) # сеикакл
#  print(text[::6]) # сеикакл
#  text = text[2:9] + text[-5] + text[:2] # ...

#              фУНЦИИ  
# def

def f (x):
    if x==1:
        return 'Целое'
    elif x == 2:
        return 23
    else:
        return
arg = 2
print (f(arg))
print (type(f(arg)))