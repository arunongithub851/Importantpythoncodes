class gtng_crct_lst:

    def __init__(self, pslst, value):
        self.name = value
        self.lst = []
        self.lst = self.lst + pslst
        self.lst.append(value)



n = int(input())
keys = [1, 2, 3]
values = [0, 0]
initiat = []
intrnums = [None, gtng_crct_lst(initiat, 1)]
for i in range(2, n + 1):
    if i - 1 > 0:
        values.append(values[i - 1] + 1)
        intrnums.append(gtng_crct_lst(intrnums[i - 1].lst, i))
    if i % 2 == 0 and i // 2 != 0:
        if values[i // 2] + 1 <= values[i]:
            values[i] = values[i // 2] + 1
            intrnums[i] = gtng_crct_lst(intrnums[i // 2].lst, i)
    if i % 3 == 0 and i // 3 != 0:
        if values[i // 3] + 1 <= values[i]:
            values[i] = values[i // 3] + 1
            intrnums[i] = gtng_crct_lst(intrnums[i // 3].lst, i)


print(values[n])
for i in intrnums[n].lst:
    print(i, end=" ")
