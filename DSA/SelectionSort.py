my_array = []

n = int(input("Enter the total number of elements: "))

for i in range(n):
    element = int(input(f"Enter element[{i+1}]: "))
    my_array.append(element)

for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
        if my_array[j] < my_array[min_index]:
            min_index = j

    min_value = my_array.pop(min_index)
    my_array.insert(i,min_value)

print(my_array)
