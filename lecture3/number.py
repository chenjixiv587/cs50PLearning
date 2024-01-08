def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            # if error in this
            print("x is not a integer")
        else:
            # if no error in this
            return x
main()