#counting character occurance


def count_char(s):
    count = {}
    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    return count
word = input("Enter a word: ")
print(count_char(word))
