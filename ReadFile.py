#for i in range(3):
    #print (i)
    #f = open("test.txt", "r")
    #firstLine = f.readline(10)
    #print(firstLine)

    #if firstLine in open("test/test.txt").read():
    #    print(firstLine + "--> exist")

print("File name (and route if its necessary) to comparate (add the file type too - test.txt) ")
s = input()
print("File name 2 to comparate (add route if its necessary)")
r = input()
print("input1 : " + s + "/ input2 :" + r)
    #Example 1
fileHandler = open (s, "r") #fileHandler = open ("test.txt", "r")
    # Get list of all lines in file
listOfLines = fileHandler.readlines()
    # Close file
fileHandler.close()

    # Iterate over the lines
for line in listOfLines:
    #print(line.strip())
    if line.strip() in open(r).read(): #if line.strip() in open("test/test.txt").read():
        print(line.strip() + " ---> exits")
    else:
        print(line.strip() + " ---> not exist")
    print ("Iteration: " + str(line) + "----------------------")
