#write functions here, don't add input('') statements here!
def test_config():
    return True

def create_multiplication_table():
    list0 = []
    for i in range(5):
        row_list = []
        for j in range(10):
            row_list.append((i + 1) * (j + 1))
        list0.append(row_list)
    return list0

def display_multiplication_table():
    list0 = create_multiplication_table()
    for row_list in list0:
        for item in row_list:
            print(str(item).rjust(3, " "), end = " ")

        print(" ")