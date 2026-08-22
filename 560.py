x = list(map(int, input("Enter: ").split()))
k = int(input("Enter target: "))
def long(x):
    count = 0
    for i in range(len(x)):
        sum = 0
        for j in range(i,len(x)):
            sum += x[j]
            if sum == k:
                count += 1
    return count
print(long(x))

def optimal(x):
    ps = 0
    c = 0
    d = {0:1}
    for num in x:
        ps += num
        val = ps-k
        if val in d:
            c += d[val]
        if ps in d:
            d[ps] += 1
        else:
            d[ps] = 1
    return c
print(optimal(x))