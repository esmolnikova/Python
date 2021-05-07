#5.A
a=[57.8, 46.51, 97, 12.32, 16, 28, 25.94, 16.11, 18.02, 2.04]
b=[]
for i in a:
    r = int(i)
    kk = int((i*100) % 100)
    p = f'{r} руб {kk:02d} коп'
    b.append(p)
price=', '.join(b)
print(price)
#5B
print(id(a))
a.sort()
print(id(a))
print(a)
#5C
a_reversed = list(reversed(a))
print(id(a_reversed))
print(a_reversed)
#5D
max_price = a_reversed[:5]
print(id(max_price))
print(max_price)
