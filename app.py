with open(r'sub_file.txt', 'r') as file:
    data = file.readlines()

for index, item in enumerate(data):

    print(index+1)
    # changed_string = string.replace("b", "B")
    item = item.replace("[", "")
    item = item.replace("]", "")
    item = item.replace("  ", "\n")
    print(item)