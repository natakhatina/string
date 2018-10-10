import random,string
# УБРАТЬ ЦИФРЫ ИЗ СТРОКИ
# a='Сегодня 4 октября'
# print(a)
# for i in range(0,10):
#     i=str(i)
#     if a.find(i)>0:
#         a=a.replace(i,'')
# print(a)

# УБРАТЬ ЗАГЛАВНЫЕ БУКВЫ ИЗ СТРОКИ
# b='abcVgT7J' #первый вариант
# print(b)
# for e in b:
#     e=ord(e)
#     if e>=65 and e<=90:
#         e=chr(e)
#         b=b.replace(e,'')
#
# print(b)

# b='abcVgT7J' # второй вариант
# print(b)
# for e in b:
#     if e>='A' and e<='Z':
#         b=b.replace(e,'')
#
# print(b)

n=6
r=random.randint(n+1,50)
b=''
b=b.join(random.choice(string.printable) for x in range(r))
print(b)
a=''
for i in range(0,len(b),n):
    a=a+b[i:i+n]+'/'
a=a[:-1]
print(a)
a=a.split('/')
print(a)
print('Результат фильтрации:')
for i in a:
    flag=0
    for j in i:
        if j >= 'A' and j <= 'Z':
            flag=flag+1
    if flag==0:
        print(i)
    

