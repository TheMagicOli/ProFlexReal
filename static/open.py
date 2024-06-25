a = open("values.txt", "r")
sheets = [[], [], [], [], [], []]
i = 0
final = ""
for char in a:
    if char == " " or char == "\n":
        sheets[i].append(final)
        i += 1
        if i == 5:
            i = 0
    else:
        final = final + char
print(sheets)


    