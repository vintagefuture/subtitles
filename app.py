with open(r'sub_file.txt', 'r') as file:
    data = file.readlines()

for index, item in enumerate(data):
    print(index)
    print(item)