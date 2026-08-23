x = list(map(int, input("Enter: ").split()))
t = int(input("Enter target: "))
def rotate(arr,k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == k:
            return mid
        if arr[left] <= arr[mid]: #if left side is sorted
            if arr[left] <= k <arr[mid]:
                right = mid-1
            else:
                left = mid+1
        else: #else right side is sorted
            if arr[mid] < k <= arr[right]:
                left = mid+1
            else:
                right = mid-1
    return -1
print(rotate(x,t))