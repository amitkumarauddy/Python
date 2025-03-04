my_array = []

n = int(input("Enter total number of elements: "))

for i in range(n):
    elements = int(input(f"Enter element [{i+1}]: "))
    my_array.append(elements)


for i in range(1,n):
    insert_index = i
    current_value = my_array.pop(i)

    for j in range(i-1, -1 , -1):
        if my_array[j] > current_value:
            insert_index = j

    my_array.insert(insert_index,current_value)


print(my_array)