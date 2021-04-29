sum_tot=0
sum_tot_b=0
i = 1
a = []
while i < 1000:
    if i % 2:
        num = i * i * i
        num_b = num + 17
        a.append(num)
        ed = num % 10
        ed_b = num_b % 10
        ten = num % 100 // 10
        ten_b = num_b % 100 // 10
        hun = num % 1000 // 100
        hun_b = num_b % 1000 // 100
        th = num % 10000 // 1000
        th_b = num_b % 10000 // 1000
        ten_th = num % 100000 // 10000
        ten_th_b = num_b % 100000 // 10000
        hun_th = num % 1000000 // 100000
        hun_th_b = num_b % 1000000 // 100000
        mil = num % 10000000 // 1000000
        mil_b = num_b % 10000000 // 1000000
        ten_mil = num % 100000000 // 10000000
        ten_mil_b = num_b % 100000000 // 10000000
        hun_mil = num % 1000000000 // 100000000
        hun_mil_b = num_b % 1000000000 // 100000000
        th_mil = num % 10000000000 // 1000000000
        th_mil_b = num_b % 10000000000 // 1000000000
        sum_3 = ed + ten + hun + th + ten_th + hun_th + mil + ten_mil + hun_mil + th_mil
        sum_3_b = ed_b + ten_b + hun_b + th_b + ten_th_b + hun_th_b + mil_b + ten_mil_b + hun_mil_b + th_mil_b
        if not sum_3 % 7 and not sum_3_b % 7:
            sum_tot += num
            sum_tot_b += num_b
            i += 1
        elif not sum_3 % 7:
            sum_tot += num
            i += 1
        elif not sum_3_b % 7:
            sum_tot_b += num_b
            i += 1
        else:
            i += 1
    else:
        i += 1
print(a)
print(sum_tot)
print(sum_tot_b)