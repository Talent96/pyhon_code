words = ["my", "self", "improve"]
capitalize_words = map(lambda x: x.capitalize(), words)
print(list(capitalize_words))

# note, x.capitalize(), capitalizes only the initials i.e the first letters of each word only.
# while str.upper(x) changes all the words to capital letters.
