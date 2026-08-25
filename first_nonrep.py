x = input("Enter: ")
def nonrep(x):
    d = {}
    for i in range(len(x)):
        if x[i] in d:
            d[x[i]] += 1
        else:
            d[x[i]] = 1
    for i in range(len(x)):
        if d[x[i]] == 1:
            return x[i]
print(nonrep(x))