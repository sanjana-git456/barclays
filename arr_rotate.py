x = list(map(int, input("Enter: ").split()))
k = int(input("Enter k: "))
def rotate(x,k):
    t = k+1
    l1 = x[t:]
    l2 = x[:t]
    return l1+l2
print(rotate(x,k))