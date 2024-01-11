import csv

students = []
with open("students_dict.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students.append(row)
        # students.append({"name": row["name"], "address": row["address"]})

for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} is from {student['address']}")


