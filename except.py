x = list(map(int, input("Enter: ").split()))
def prod(x):
    result = []
    left = [1]*len(x)
    right = [1]*len(x)
    for i in range(1,len(x)):
        left[i] = left[i-1] * x[i-1]
    for i in range(len(x)-2,-1,-1):
        right[i] = right[i+1] * x[i+1]
    for i in range(len(x)):
        result.append(left[i]*right[i])
    return result
print(prod(x))