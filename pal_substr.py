x = input("Enter: ")
def expand(x,left,right):
    while left >= 0 and right < len(x) and x[left] == x[right]:
        left -= 1
        right += 1
    return x[left+1:right]
def long(x):
    longest = ""
    for i in range(len(x)):
        odd = expand(x,i,i) #when length is odd so single centre point
        even = expand(x,i,i+1) #when length is even so 2 centre points
        if len(odd) > len(longest):
            longest = odd
        if len(even) > len(longest):
            longest = even
    return longest
print(long(x))