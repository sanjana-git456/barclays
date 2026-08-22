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