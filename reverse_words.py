x = input("Enter: ")
def rev(x):
    x = x.split()
    return x[::-1]
print(' '.join(rev(x)))

def manual(x):
    words = []
    word = ""
    result = []
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
    for i in range(len(words)-1,-1,-1):
        result.append(words[i])
    return ' '.join(result)
print(manual(x))