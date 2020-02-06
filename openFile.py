"""openFile.py

Reads a file containing scores then prints the data as-is, sorts and prints and then reverses
and prints
"""

scores = []					# Array to hold scores
names = [] 					# Array to hold names

result_f = open('results.txt')
for line in result_f:
	(name,score) = line.split()
	scores.append(float(score))
	names.append(name)

result_f.close()
print("The contents of the results file:")

i = 0
for i in range(len(scores)):
	print(names[i] + ' with ' + str(scores[i]))

scores.sort()
names.sort()

print("The contents after a sort:")

for i in range(len(scores)):
	print(names[i] + ' with ' + str(scores[i]))

scores.reverse()
names.reverse()

print("The contents after a reverse:")

for i in range(len(scores)):
	print(names[i] + ' with ' + str(scores[i]))
