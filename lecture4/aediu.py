"""
# JOIN WORDS INTO A LIST:

mylist = p.join(("apple", "banana", "carrot"))
# "apple, banana, and carrot"

mylist = p.join(("apple", "banana"))
# "apple and banana"

mylist = p.join(("apple", "banana", "carrot"), final_sep="")
# "apple, banana and carrot"

"""

import inflect
p = inflect.engine()

l_names = []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    else:
        l_names.append(name)
t_names = tuple(l_names)
o_base = "Adieu, adieu, to "
output = o_base + p.join(t_names)
print(output)
