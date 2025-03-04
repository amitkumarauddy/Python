a = []

n = int((input("Enter the total number of elements: ")))

for i in range(n):
    element = int(input(f"Enter element [{i+1}] to be bubble sorted: "))
    a.append(element)


for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)