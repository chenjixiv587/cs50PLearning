# match 
name = input("What is your name? ").upper()

match name:
    case "A" | "F" | "V":
        print("Good")
    case "B":
        print("Good")
    case "C":
        print("Good")
    case "D":
        print("No")
    case _:
        print("Who? ")