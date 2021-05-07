b =[15*3, 15/3, 15//2, 15**2, 15==2, {15, 2}, (15, 3), [15, 2], '"15*3"']
for i in b:
    if (type(i) == int):
        print(i, 'тип данных - int'),
    elif (type(i) == bool):
        print(i, 'тип данных boolean'),
    elif (type(i) == list):
        print(i, 'тип данных - list'),
    elif (type(i) == str):
        print(i, 'тип данных - str'),
    elif (type(i) == float):
        print(i, 'тип данных - float'),
    elif (type(i) == set):
        print(i, 'тип данных - set'),
    elif (type(i) == tuple):
        print(i, 'тип данных - tuple'),
    else:
        print(i, 'неизвестный тип данных')
# возможно ли вывести не результат i, а сами выражения не "45", а "15*3" в print?