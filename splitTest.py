x = 'blue,red,green'
y = x.split(",")

print(y)


f = open("testfile.txt", "r")
f1 = open("outputtest.txt", "w")

for eachLine in f:
    splittedLine = eachLine.split(",")
    print(splittedLine)
    f1.write(str(splittedLine))
f.close()
f1.close()
