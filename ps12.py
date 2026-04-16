N = 4
for i in range(1, N+1):
    for j in range(1, N - i + 1):
        print(' ', end='')
    
    if i == 1:
        print('*', end='')
    else:
        print('*', end='')  
        for k in range(1, 2*i - 2):
            print(' ', end='')
        
        print('*', end='')   
    
    print()
for i in range(N-1, 0, -1):
    for j in range(1, N - i + 1):
        print(' ', end='')
    
    if i == 1:
        print('*', end='')
    else:
        print('*', end='')
        
        for k in range(1, 2*i - 2):
            print(' ', end='')
        
        print('*', end='')
    
    print()