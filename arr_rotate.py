x = list(map(int, input("Enter: ").split()))
k = int(input("Enter k: "))
def rotate(x,k):
    l1 = x[k:]
    l2 = x[:k+1]
    return l1+l2
print(rotate(x,k))