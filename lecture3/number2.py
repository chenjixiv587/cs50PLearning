def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x?, you know x must be an integer "))
        except ValueError:
            # if error in this
            pass
main()