numbers = [34, 78, 12, 90, 45, 67]

max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Maximum =", max_num)
print("Minimum =", min_num)