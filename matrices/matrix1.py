def matrices(r,c):
    m1 = [[0 for _ in range(c)] for _ in range(r)]
    m2 = [[0]*c for _ in range(r)]
    return m1,m2
print(matrices(3,4))