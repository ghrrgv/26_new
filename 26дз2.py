f = open('26_2web')
# наибольшее кол-во cколько сможет увести, кол-во сколько не сможет увести\
vmestimost, n = map(int, f.readline().split())
produkri = []
podoshel = []
ne_podoshel = []
for s in f:
    produkri.append(int(s))
podoshel.sort()
for produkt in produkri:
    if sum(podoshel) + produkt <= vmestimost:
        podoshel.append(produkt)
    else:
        ne_podoshel.append(produkt)
print(len(podoshel), len(ne_podoshel))
\\\