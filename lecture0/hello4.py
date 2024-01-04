# the default para
# 变量需要先定义 再使用 靠近使用的地方进行定义
def main():
    name:str = input("What is your name? ").strip().title()
    hello(name)
def hello(to:str="world"):
    print("hello, ", to)
if __name__ == "__main__":
    main()

