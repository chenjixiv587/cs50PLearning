def main():
    x:int = int(input("What's x?"))
    print("x squares is, ", square(x))

def square(n:int)->int:
    """
    Return the n ** 2
    """
    return n * n

if __name__ == "__main__":
    main()
