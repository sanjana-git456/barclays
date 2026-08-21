x = list(map(int, input("Enter: ").split()))
def profit(x):
    best = 0
    for i in range(len(x)):
        left = x[:i]
        right = x[i:]
        total = logic(left) + logic(right)
        best = max(best,total)
    return best
def logic(x):
    if not x:
        return 0
    minprice = x[0]
    m = 0
    for price in x:
        m = max(m, price - minprice)
        minprice = min(price,minprice)
    return m
print(profit(x))