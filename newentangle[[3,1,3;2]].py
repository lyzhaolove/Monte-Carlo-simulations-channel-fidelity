import random
T = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # I,X1,X2
     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # X3,Z1,Z2
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],  # Z3,Y1,Y2
     [0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 1, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],  # Y3,X2Y3,Z2X3
     [0, 1, 0, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 0, 0],  # Y2Z3,X1Z3,Z1Y3
     [1, 0, 1, 0, 0, 1, 0, 0, 0, 0]]  # Y1X3
G = [[1, 0, 0, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
     [1, 1, 0, 0, 0, 1, 1, 1, 0, 1]]                                                                   # 生成元

S = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 稳定子群
# 把G中每个元素添加到S中
for i in range(4):
    S.append(G[i])

# 下面是两个元素的异或运算
for i in range(4):
    for j in range(i+1, 4):
        s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for t in range(10):
            s[t] = G[i][t] ^ G[j][t]
        S.append(s)
# 下面是三个元素的异或运算
for i in range(4):
    for j in range(i+1, 4):
        for k in range(j+1, 4):
            s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for t in range(10):
                s[t] = G[i][t] ^ G[j][t] ^ G[k][t]
            S.append(s)
# 下面是四个元素的异或运算
s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for t in range(10):
    s[t] = G[0][t] ^ G[1][t] ^ G[2][t] ^ G[3][t]
S.append(s)
print(S)
print(len(S))

E = []
for i in range(16):
    for j in range(4):
        e = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for t in range(10):
            e[t] = T[i][t] ^ S[j][t]
        E.append(e)
print("E=", E)
print(len(E))

for q in range(21):
    rate = 0.01
    rate *= q
    count = 0
    probability = 0
    # print("rate=", rate)
    for k in range(1000):
        D = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        r0 = random.random()
        r1 = random.random()
        r2 = random.random()
        r3 = random.random()
        r4 = random.random()
        if r0 < rate:
            r0 = int(4 * r0 / rate)
            if r0 & 1 == 0 and r0 >> 1 == 0:
                D[0] = 0
                D[5] = 0
            elif r0 & 1 == 1 and r0 >> 1 == 0:
                D[0] = 1
                D[5] = 0
            elif r0 & 1 == 0 and r0 >> 1 == 1:
                D[0] = 0
                D[5] = 1
            elif r0 & 1 == 1 and r0 >> 1 == 1:
                D[0] = 1
                D[5] = 1
        if r1 < rate:
            r1 = int(4 * r1 / rate)
            if r1 & 1 == 0 and r1 >> 1 == 0:
                D[1] = 0
                D[6] = 0
            elif r1 & 1 == 1 and r1 >> 1 == 0:
                D[1] = 1
                D[6] = 0
            elif r1 & 1 == 0 and r1 >> 1 == 1:
                D[1] = 0
                D[6] = 1
            elif r1 & 1 == 1 and r1 >> 1 == 1:
                D[1] = 1
                D[6] = 1
        if r2 < rate:
            r2 = int(4 * r2 / rate)
            if r2 & 1 == 0 and r2 >> 1 == 0:
                D[2] = 0
                D[7] = 0
            elif r2 & 1 == 1 and r2 >> 1 == 0:
                D[2] = 1
                D[7] = 0
            elif r2 & 1 == 0 and r2 >> 1 == 1:
                D[2] = 0
                D[7] = 1
            elif r2 & 1 == 1 and r2 >> 1 == 1:
                D[2] = 1
                D[7] = 1
        if r3 < 0.5 * rate:
            r3 = int(4 * r3 / (0.5 * rate))
            if r3 & 1 == 0 and r3 >> 1 == 0:
                D[3] = 0
                D[8] = 0
            elif r3 & 1 == 1 and r3 >> 1 == 0:
                D[3] = 1
                D[8] = 0
            elif r3 & 1 == 0 and r3 >> 1 == 1:
                D[3] = 0
                D[8] = 1
            elif r3 & 1 == 1 and r3 >> 1 == 1:
                D[3] = 1
                D[8] = 1
        if r4 < 0.5 * rate:
            r4 = int(4 * r4 / (0.5 * rate))
            if r4 & 1 == 0 and r4 >> 1 == 0:
                D[4] = 0
                D[9] = 0
            elif r4 & 1 == 1 and r4 >> 1 == 0:
                D[4] = 1
                D[9] = 0
            elif r4 & 1 == 0 and r4 >> 1 == 1:
                D[4] = 0
                D[9] = 1
            elif r4 & 1 == 1 and r4 >> 1 == 1:
                D[4] = 1
                D[9] = 1
            # print("rate=",rate)

        if D in E:
            count += 1

    probability = count / 1000
    print(probability, end=', ')
