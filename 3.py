tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', "Александр", "Станислав"
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def nums():
    for idx, name in enumerate(tutors):
        if idx < len(klasses):
            num = (name, klasses[idx])
        else:
            num = (name, None)
        print(num)
        yield idx

gener = nums()
for num in gener:
    print(num)
for num in gener:
    print(num)