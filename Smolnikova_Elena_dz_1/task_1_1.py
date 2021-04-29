duration=36060
d=duration//86400
h=(duration-d*86400)//3600
m=(duration-(d*86400+h*3600))//60
s=duration%60
if d>0:
    print(d, 'дн',h, 'час', m, 'мин', s,'сек')
else:
    if h>0:
        print(h, 'час', m, 'мин', s, 'сек')
    else:
        if m>0:
            print(m, 'мин', s, 'сек')
        else:
            print(s, 'сек')

# ниже, если вывод нулевых временных единиц не нужен вообще, а не только в начале

duration=1505460
d=duration//86400
h=(duration//3600)% 24
m=(duration//60) % 60
s=duration % 60
if duration==0:
    print('0 сек')
else:
    if not d:
        d=''
    else:
        d = str(d) + ' д'
    if not h:
        h = ''
    else:
        h = str(h) + ' час'
    if not m:
        m = ''
    else:
        m = str(m) + ' мин'
    if not s:
        s = ''
    else:
        s = str(s) + ' сек'
    print(d, h, m, s)