sorted_names = []
with open("names.txt") as f:
    for name in f:
        sorted_names.append(name.rstrip())
for name in sorted(sorted_names):
    print(name)