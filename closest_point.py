x = eval(input("Enter: "))
k = int(input("Enter k: "))
def closest(p,t):
    dist = []
    result = []
    for i in x:
        d = i[0]**2 + i[1]**2
        dist.append((d,i))
    dist.sort()
    for i in dist[:k]:
        result.append(i[1])
    return result
print(closest(x,k))