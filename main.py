import math
with open("laracroft.txt", mode='r', encoding='UTF-8') as text:
    reader = text.read()
    new_dict2 = {}
    lisT = []
    lisT2 = []
    z = 1
    x = 0
    count = 0
    for i in reader:
        new_dict2[z] = reader[count:count + 8]
        lisT.append(i)
        lisT2.append(i)
        x += 1
        if x == 8:
            z += 1
            count += 8
            x = 0
print(new_dict2)
print(lisT)
lisT = list(map(int, lisT))
lisT2 = list(map(int, lisT))
print(lisT2)
# Частотный побитовый тест.
for i in range(len(lisT)):
    if lisT[i] == 0:
        lisT[i] = -1
print(lisT)
print(sum(lisT))
S1 = (1 / math.sqrt(128)) * sum(lisT)
print(S1)  # S1 = 0.8838834764831843
P1 = math.erfc(S1 / math.sqrt(2))
print(P1)  # P1 = 0.37675911781158217

# Тест на одинаковые подряд идущие биты.
S2 = (1 / 128) * sum(lisT2)
print(S2)  # S2 = 0.5390625
if abs(S2 - 0.5) < 2 / math.sqrt(128):
    print("Ok lets go!!!!!!!")
else:
    print("Oh sorry and we are go again")
ri = []
for i in range(len(lisT2) - 1):
    if lisT2[i] == lisT2[i + 1]:
        ri.append(0)
    else:
        ri.append(1)
print(ri)
Vn = sum(ri)
print(Vn)
P2 = math.erfc((abs(Vn - 2 * 128 * S2 * (1 - S2))) / (2 * math.sqrt(2 * 128) * S2 * (1 - S2)))
print(P2)  # P2 = 0.804645310694816
# Тест на самую длинную последовательность единиц в блоке.
lisT3 = []
for k, v in new_dict2.items():
    max2 = 1
    for i in range(len(v)):
        max1 = 0
        if v[i] == "1":
            z = i
            while v[z: z + 1] == "1":
                z += 1
                max1 += 1
        if max1 > max2:
            max2 = max1
    lisT3.append(max2)
print(lisT3)
v1 = lisT3.count(1)
v2 = lisT3.count(2)
v3 = lisT3.count(3)
v4 = lisT3.count(4) + lisT3.count(6)
X2 = 0
X2 += ((v1 - 16 * 0.2148) ** 2) / (16 * 0.2148)
X2 += ((v2 - 16 * 0.3672) ** 2) / (16 * 0.3672)
X2 += ((v3 - 16 * 0.2305) ** 2) / (16 * 0.2305)
X2 += ((v4 - 16 * 0.1875) ** 2) / (16 * 0.1875)
print(X2)
# X^2 = 0.6526312412476418