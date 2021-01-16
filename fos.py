import time
start = time.time()
colin_hist = [0] * 36
for a in range(1,7):
    for b in range(1, 7):
        for c in range(1, 7):
            for d in range(1, 7):
                for e in range(1, 7):
                    for f in range(1, 7):
                        index = a+b+c+d+e+f
                        colin_hist[index - 1] += 1
peter_hist = [0] * 36
for a in range(1,5):
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                for e in range(1, 5):
                    for f in range(1, 5):
                        for g in range(1, 5):
                            for h in range(1, 5):
                                for i in range(1, 5):
                                    index = a+b+c+d+e+f+g+h+i
                                    peter_hist[index - 1] += 1
count = 0
a = 0
b = 0
while b < len(peter_hist):
    while a < len(colin_hist):
        if b > a and peter_hist[b] != 0 and colin_hist[a] != 0:
            count += peter_hist[b] * colin_hist[a]
        a += 1
    a = 0
    b += 1
total_possiblities = (4**9)*(6**6)
print(f"{(count / total_possiblities):.7f}")
print(time.time() - start)