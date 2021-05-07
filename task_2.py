
#1-49 2-50 3-51 4-52 5-53 6-54 7-55, 8-56 9-57 0-48 +-43 -45
a=['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
c=[]
for i in a:
    if (ord(i[0]) == 43) or (ord(i[0]) == 45):
        b=int(i)
        b = f'{b:02d}'
        c.append('"')
        c.append(chr(ord(i[0])))
        c.append(b)
        c.append('"')
    elif (48 < ord(i[0]) < 57):
        i=int(i)
        b = f'{i:02d}'
        c.append('"')
        c.append(b)
        c.append('"')
    else:
        c.append(i)
print(c)
p=f' '.join(c)
print(p)

