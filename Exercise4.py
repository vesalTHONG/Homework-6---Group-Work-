array = [5, 4, 7, 3, 4, 5, 4]
newArray = []

def chunk(array, size):
    for i in range(0, len(array), size):
        newArray.append(array[i:i+size])
    return newArray


print(chunk(array,5))
print(chunk(array,3))