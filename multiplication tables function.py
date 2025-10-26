def tabl(num):
    output = ""
    for i in range(11):
        product = num * i
        line = str(num) + " " + "x" + " " + str(i) + " " + "=" + " " + str(product)
        if i != 11:
            output = output + line + "\n"
    return output

# print(tabl(3))