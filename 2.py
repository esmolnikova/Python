
#A - 65 a 97
#z - 90 z 122
def num_translate(a):
    number_eng_rus = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }
    if 65 < (ord(a[0])) < 97:
        print('"', number_eng_rus.get(a.lower()).capitalize(), '"', sep=''),
    else:
        print('"', number_eng_rus.get(a), '"', sep='')


num_translate("Ten")

