src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

result_new = [num for idx, num in enumerate(src) if (src[idx] > src[idx-1]) and (idx > 0)]
print(result_new)