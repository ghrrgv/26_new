f = open('26_5web')
n, budget, k = 6536, 165589, 123
\
osnovniye_cena = []
ugosheniya_cena = []
summ_osnovniye = 0
ugosheniya = []
for s in f:
    if 'A' in s:
        osnovniye_cena.append(int(s[:-2]))
    else:
        ugosheniya_cena.append(int(s[:-2]))

osnovniye_cena.sort()
for i in range(123):
    summ_osnovniye += osnovniye_cena[i]
ugosheniya_cena.sort()
for t in ugosheniya_cena:
    if (sum((list(osnovniye_cena + ugosheniya_cena))[:n//4]))*0.33 < budget:
        ugosheniya.append(t)
print(sum(ugosheniya))
skidka = sum(list(osnovniye_cena + ugosheniya_cena)[:n//4])*0.33
print(skidka)