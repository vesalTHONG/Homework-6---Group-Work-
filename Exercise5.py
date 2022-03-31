string = input('Enter any string to reverse: ')
reversed = ""
index = len(string) 
while index > 0: 
    reversed += string[index - 1] 
    index = index - 1
print(reversed)
