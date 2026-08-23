x = eval(input("Enter: "))
def merge(arr):
    arr.sort()
    result = [arr[0]]
    for i in range(1,len(arr)):
        last = result[-1]
        print("last = ",last)
        curr = arr[i]
        print("Curr= ",curr)
        if curr[0] <= last[1]:
            last[1] = max(last[1],curr[1])
            print("new last: ",last)
        else:
            result.append(curr)
            print("result: ",result)
    return result
print(merge(x))