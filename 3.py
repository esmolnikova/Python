def currency_rates(*args):

    from requests import get, utils
    import datetime as DT
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    a = content.split('"Foreign Currency Market">')
    b = a[0].split('Date=')
    b = b[1].split( )
    a = a[1].split('</Valute>')
    j = []
    for i in a:
        i = i.split('><')
        j.append(i)
    j.pop()
    v = 'None'
    for i in j:
        char_code = i[2].split('</')
        char_code = char_code[0].split('>')
        nominal = i[3].split('</')
        nominal = nominal[0].split('>')
        value = i[5].split('</')
        value = value[0].split('>')
        value = value[1].split(',')
        value = int(value[0])+(int(value[1]))/10000
        val = {'char_code': char_code[1], 'nominal': nominal[1], 'value': value}
        for arg in args:
            if arg.upper() == char_code[1]:
                v = f'{int(nominal[1]):d} {char_code[1]} {value}'
                print(v)
    if v == 'None':
        print(v)
    b = str(b[0])
    dt = DT.datetime.strptime(b,'"%d.%m.%Y"').date()
    print(dt)

currency_rates('usd', 'eur')