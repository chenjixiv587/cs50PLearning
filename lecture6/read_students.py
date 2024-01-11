def main():
    file_stuents = "students.csv"
    students = read_students(file_stuents)
    show(students)


# Read the file
def read_students(file_name: str):
    students = []
    with open(file_name, "r") as file:
        for line in file:
            name, address = line.rstrip().split(",")
            student = {"name": name, "address": address}
            students.append(student)
    return students


# Get the name to sort
def get_name(student: dict):
    return student["name"]

# key specifies a function of one argument that is used to extract a comparison key from each element in iterable 
# (for example, key=str.lower). 
# The default value is None (compare the elements directly).
# key 是一个函数 主要对可迭代对象里面的每个元素进项操作 作为排序的依据 在这里就是对  student 进行操作
# Get the name, address
def show(students: list):
    # key = lambda student: student["name"]
    for student in sorted(students, key=get_name):
        print(f"{student['name']} is living in {student['address']}")


if __name__ == "__main__":
    main()
