f = open('26_4web')
n = int(f.readline())
tovari = []
for s in f:
    tovari.append(int(s))
# минимальная цена которую хотел заплатить и которую заплатил
tovari.sort(reverse=True)
skidka = sum(tovari[:len(tovari) // 3])
print(sum(tovari) - skidka)
summ = sum(tovari)
for i in range(2, len(tovari), 3):
    summ -= tovari[i]
print(summ)