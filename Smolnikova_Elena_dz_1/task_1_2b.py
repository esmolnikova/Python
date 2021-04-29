sum_tot=0
i = 1
a = []
while i < 1000:
    if i % 2:
        num = i * i * i
        a.append(num)
        ed = num % 10
        ten = num % 100 // 10
        hun = num % 1000 // 100
        th = num % 10000 // 1000
        ten_th = num % 100000 // 10000
        hun_th = num % 1000000 // 100000
        mil = num % 10000000 // 1000000
        ten_mil = num % 100000000 // 10000000
        hun_mil = num % 1000000000 // 100000000
        th_mil = num % 10000000000 // 1000000000
        sum_3 = ed + ten + hun + th + ten_th + hun_th + mil + ten_mil + hun_mil + th_mil
        if not sum_3 % 7:
            sum_tot += num
            i += 1
        else:
            i += 1
    else:
        i += 1
print(a)
print(sum_tot)
b = []
sum_tot_b = 0
k=0
while k<len(a):
    num_b = a[k] + 17
    b.append(num_b)
    ed = num_b % 10
    ten = num_b % 100 // 10
    hun = num_b % 1000 // 100
    th = num_b % 10000 // 1000
    ten_th = num_b % 100000 // 10000
    hun_th = num_b % 1000000 // 100000
    mil = num_b % 10000000 // 1000000
    ten_mil = num_b % 100000000 // 10000000
    hun_mil = num_b % 1000000000 // 100000000
    th_mil = num_b % 10000000000 // 1000000000
    sum_3 = ed + ten + hun + th + ten_th + hun_th + mil + ten_mil + hun_mil + th_mil
    if not sum_3 % 7:
        sum_tot_b += num_b
        k += 1
    else:
        k += 1
else:
    k += 1
print(b)
print(sum_tot_b)