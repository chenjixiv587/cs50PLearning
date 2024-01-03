# Ask for user name 
name:str = input("What is your name? \n").strip().title()

# echo the name
l_name:list = name.split(" ")
first_name, last_name = l_name
# print("hello, " + s_name, sep="", end="")
print(f"hello {name}")
print(l_name)
print(first_name, last_name)
# learn the things 