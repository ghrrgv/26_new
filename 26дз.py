def chet(n):
    if n % 2 == 0: return True
def nechet(n):
    if n % 2 != 0: return True

f = open('inf_26_04_21_26.txt')
N = int(f.readline())
a = [int(x) for x in f]
summ = 0
summ_max = []
for i in range(N-1):
    if ((chet(a[i]) and nechet(a[i+1])) or (nechet(a[i]) and chet(a[i+1]))) == True:
        summ = a[i] + a[i-1]
        if summ in a:
            summ_max.append(summ)
print(len(summ_max), max(summ_max))