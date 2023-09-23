def matrices(r,c):
    m1 = [[0 for _ in range(c)] for _ in range(r)]
    m2 = [[0]*c for _ in range(r)]
    for i in range(c):
        s = [r[i] for r in m1]
        print(s)
matrices(3,4)