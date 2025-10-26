#Reading file
file1 = open("FileName", "r")  #r is read mode
file2 = open("FileName", "w")  #w is write mode
file3 = open("FileName", "a")  #a is append mode

#ALWAYYYYS REMEMBERRRR TO CLOSEE FILEEE
text = file1.read().strip()  #strip for removing whitespace character
file1.close()

#reading a single line
first = file2.readline()
file2.close()

#Writing a new file
file4 = open("NewFile.txt", "w")
file4.write("AppleJuice\n")
file4.close()

#Writing in an existing file
file5 = open("NewFile.txt", "a")
file5.write("AppleJuice\n")
file5.write("AppleJuice\n")
file5.close()


#Exception Handling
try:
    Num = int(input("Enter a number: "))
except ValueError:
    print("Integer Only")

try:
    Num = 5/0
    print(Num)
except ZeroDivisionError:
    print("Can not divide by zero")

try:
    file6 = open("File.txt", "r")
except IOError:
    print("File does not exist")

    
array = [""] * 7
try:
	for i in range(0, 10):    # ⚠️ loops more times than array length
		array[i] = "green"
		print(array)        #can't print from i = 7 onwards!
except IndexError:
	print("Invalid array index")