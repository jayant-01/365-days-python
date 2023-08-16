#palindrome word


def palindrome(s):
    return s == s[::-1]

# finding palindrome words in a sentence

s = input("Enter a sentence: ")
words = s.split(" ")
lst = []
for word in words:
    if palindrome(word):
        lst.append(word)
print(lst)

