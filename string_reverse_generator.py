def string_rev(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
        yield my_str[i]
rev_word= []
for char in string_rev("reverse"):
    rev_word.append(char)
print ("Reversed string :- "+str(''.join(rev_word)))
