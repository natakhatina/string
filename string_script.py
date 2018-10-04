#a='Сегодня 4 октября'
# for i=0:9
#     if a.find('i')>0:
#         a.replace('i','')

# if a.find('4')>0:
#     a.replace('4','')
#     print(a)

# b=a.find('4')
# print(b)
# a=a.replace('4','')
# print (a)

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

a='cajslUhsRw2/fwse68FLp3j/42372/j?kiOO'
print(a)
b=a.split('/')
print(b)
for i in b:
    print(i)
    for e in i:
