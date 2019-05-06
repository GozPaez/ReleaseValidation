#for i in range(3):
    #print (i)
    #f = open("test.txt", "r")
    #firstLine = f.readline(10)
    #print(firstLine)

    #if firstLine in open("test/test.txt").read():
    #    print(firstLine + "--> exist")

    #Example 1
fileHandler = open ("test.txt", "r")
    # Get list of all lines in file
listOfLines = fileHandler.readlines()
    # Close file
fileHandler.close()

    # Iterate over the lines
for line in listOfLines:
    #print(line.strip())
    if line.strip() in open("test/test.txt").read():
        print(line.strip() + " ---> exits")
    else:
        print(line.strip() + " ---> not exist")
    print ("Iteration: " + str(line) + "----------------------")
