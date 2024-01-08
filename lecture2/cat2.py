def main():
    number = get_number()
    memo(number)

def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            return n
def memo(n):
    for _ in range(n):
        print("memo")

if __name__ == "__main__":
    main() 