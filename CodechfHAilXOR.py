import math


def return_power(num):
    return int(math.log2(num))


for _ in range(int(input())):
    N, X = map(int, input().split())
    num_List = list(map(int, input().split()))
    i = 0
    while True:
        if X == 0:
            break
        while num_List[i] == 0 and i < N - 1:
            i = i + 1
        if i == N - 1:
            break

        reducer = 2 ** return_power(num_List[i])
        num_List[i] = num_List[i] ^ reducer
        j = i + 1
        while j < N:
            if j == N - 1:
                num_List[j] = num_List[j] ^ reducer
                break
            if num_List[j] > (num_List[j] ^ reducer):
                num_List[j] = num_List[j] ^ reducer
                break
            j = j + 1
        X = X - 1

    if X:
        if X == 1 or (X % 2 != 0 and N == 2):
            num_List[-2] = num_List[-2] ^ 1
            num_List[-1] = num_List[-1] ^ 1
    for i in num_List:
        print(i, end=" ")
    print()
