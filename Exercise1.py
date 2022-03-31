def replace_first(items: list):
    return items[1:len(items):] + items[0:1:]

print(list(replace_first([1, 2, 3, 4])))
