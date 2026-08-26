x = input("Enter: ")
def rev(x):
    x = x.split()
    return x[::-1]
print(' '.join(rev(x)))

def manual(x):
    words = []
    word = ""
    i = 0
    while i < len(x):
        if x[i] != " ":
            word += x[i]
        else:
            if word:
                words.append(word)
                word = ""
        i += 1
    if word:
        words.append(word)
    return words
print(manual(x))