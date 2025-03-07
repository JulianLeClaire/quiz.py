def zig_zag_pattern(n):
    for i in range(1, n, 2):
        print(i, end =' ')
    
    for i in range(n-3, 0, -2):
        print(i, end =' ')
zig_zag_pattern(10)
