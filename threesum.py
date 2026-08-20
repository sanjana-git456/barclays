x = list(map(int, input("Enter: ").split()))
t = int(input("Enter target: "))
def threesum(x,t):
    x = sorted(x)
    a = 0
    while a < len(x):
        right = len(x)-1
        fix = x[a]
        left = a+1
        while left < right:
            if x[left] + x[right] + fix > t:
                right -= 1
            elif x[left] + x[right] + fix < t:
                left += 1
            else:
                return x[left],x[right],fix
        a += 1
    return -1
print(threesum(x,t))