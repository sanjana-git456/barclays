x = input("Enter: ")
def rev(x):
    x = x.split()
    return x[::-1]
print(' '.join(rev(x)))