from faker import Faker


def main():
    users_num: int = 10
    users = get_user(users_num)
    file_name = "students_dict.csv"
    res = write_to(file_name, users)
    print(res)


# Get the random info of the user
def get_user(users_num: int):
    faker = Faker()
    users = []
    for _ in range(users_num):
        name = faker.name()
        address = faker.address()
        users.append({name: address})
    return users


# Write to the.csv
def write_to(file_name: str, users: list):
    with open(file_name, "a") as f:
        for user in users:
            for name, address in user.items():
                f.write(f"{name},{address}\n")
    return "Get Done!!"


if __name__ == "__main__":
    main()
