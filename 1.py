def num_translate(a):
    number_eng_rus = {
        "one": '"один"',
        "two": '"два"',
        "three": '"три"',
        "four": '"четыре"',
        "five": '"пять"',
        "six": '"шесть"',
        "seven": '"семь"',
        "eight": '"восемь"',
        "nine": '"девять"',
        "ten": '"десять"'
    }
    print(number_eng_rus.get(a))


num_translate("One")

