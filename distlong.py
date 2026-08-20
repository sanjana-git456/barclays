x = input("Enter: ")
def distinct(x):
    left = 0
    right = 1
    d = {}
    m = 0
    while right < len(x):
        if x[right] not in d:
            d[x[right]] = 1
        else:
            d[x[right]] += 1
        while len(d) > 2:
            del d[x[left]]
            left += 1
        m = max(m, right-left+1)
        right += 1
    return m
print(distinct(x))