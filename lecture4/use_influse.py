import inflect
"""
p.plural() 单数变成复数

 
"""
p = inflect.engine()

# word = input("Word: ")
# print(f"The plural of {word} is {p.plural('cat', word)}")
print("I saw", "2", p.plural("cat", "2"))
print(p.plural_noun("I"))
print(p.plural_verb("saw", 2))
print(p.plural_adj("beauty"))