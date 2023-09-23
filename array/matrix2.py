def matrices(r,c):
    m1 = [[0 for _ in range(c)] for _ in range(r)]
    m2 = [[0]*c for _ in range(r)]
    m1[1][2] = 4
    m1[2][1] =3
    for i in m1:
        print(i)
matrices(3,4)