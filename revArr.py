givenArr = [1, 2, 3, 4, 5]


def revarr(arr):
    lent = len(arr)
    # print(lent)
    for i in range(lent, 0, -1):
        print(arr[i - 1])

revarr(givenArr)
