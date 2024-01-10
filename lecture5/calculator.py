def main():
    x = get_num()
    print(f"Square x is {square(x)}")

def get_num():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

def square(n):
    return n * n


if __name__ == "__main__":
    main()
