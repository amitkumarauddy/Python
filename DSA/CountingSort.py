def countingSort(arr):
    
    max_value = max(arr)

    count_arr = [0] * (max_value + 1)

    for num in arr:
        count_arr[num] += 1

    sorted_arr = []
    
    for i in range(len(count_arr)):
        sorted_arr.extend([i] * count_arr[i])

    return sorted_arr

unsorted_arr = []

n = int(input("Enter the length of array: "))

for i in range(n):
    element = int(input(f"Enter array element[{i+1}] :"))
    unsorted_arr.append(element)

sorted_arr = countingSort(unsorted_arr)

print(sorted_arr)