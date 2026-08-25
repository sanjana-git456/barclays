x = list(map(int, input("Enter: ").split()))
k = int(input("Enter k: "))
def rotate(x,k):
    l1 = x[k:]
    l2 = x[:k]
    return l1+l2
print(rotate(x,k))

def rotate2(x, k):
    n = len(x)
    k = k % n
    def reverse(left, right):
        while left < right:
            x[left], x[right] = x[right], x[left]
            left += 1
            right -= 1
    reverse(0, k - 1)
    reverse(k, n - 1)
    reverse(0, n - 1)
    return x
print(rotate2(x,k))