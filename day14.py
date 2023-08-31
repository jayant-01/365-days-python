#textwrap program using python

import textwrap

keystring = input("enter your wraping string content")

wrapper = textwrap.TextWrapper(width=100)
word_list = wrapper.wrap(text=keystring)

print(word_list)