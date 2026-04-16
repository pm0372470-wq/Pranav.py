n=6
triangle = []
for i in range(n):
    row = [1] * (i + 1)
    
    for j in range(1, i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    
    triangle.append(row)

for i in range(n):
    print('  ' * (n - i - 1), end='')
    for num in triangle[i]:
        print(f"{num:3}", end=' ')
    
    print()