def main():
    height = int(input("What's the height? "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i)
main()