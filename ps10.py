n = 4

for i in range(1, n+1):            # rows
    for j in range(1, 2*n + 1):    # columns
        if i == 1 or i == n or j == 1 or j == 2*n:
            print('*', end='')
        else:
            print(' ', end='')
    print()