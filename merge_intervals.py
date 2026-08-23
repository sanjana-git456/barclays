x = eval(input("Enter: "))
def merge(arr):
    arr.sort()
    result = [arr[0]]
    for i in range(1,len(arr)):
        last = result[-1]
        curr = arr[i]
        if curr[0] <= last[1]:
            last[1] = max(last[1],curr[1])
        else:
            result.append(curr)
    return result
print(merge(x))