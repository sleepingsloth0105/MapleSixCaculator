'''
a = {}
a[1] = [11,22,33,44]
a[2] = [55,66,77,88]
k = a.items()
print(a.items())
for i in k:
    if [11,22,33,44] in i:
        print('in')

findkey = [k for k,v in a.items() if v == [11,22,33,44,55]]
print(findkey)
'''
a = 0.00021209322779243542 * 100
b = 1
c = b / a
print(c)
