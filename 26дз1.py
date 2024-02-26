f = open('26_1web')
vmestimost, n = map(int, f.readline().split())
#найти максимальное число упаковок, массу самой тяжёлой коробки
upakovki = []
podoshel = []
for s in f:
    upakovki.append(int(s))
upakovki.sort()
for upakovka in upakovki:
    if sum(podoshel) + upakovka <= vmestimost:
        podoshel.append(upakovka)
    elif sum(podoshel[:-1]) + upakovka <= vmestimost:
        del podoshel[-1]
        podoshel.append(upakovka)
print(len(podoshel), max(podoshel))