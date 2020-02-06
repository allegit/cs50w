"""openFile.py

Reads a file containing scores then prints the data as-is, sorts and prints and then reverses
and prints
"""

scores = []
result_f = open('results.txt')
for line in result_f:
	(name,score) = line.split()
	scores.append(float(score))
result_f.close()
print("The contents of the results file:")

i = 0
for i in range(len(scores)):
	print(scores[i])

scores.sort()

print("The contents after a sort:")

for i in range(len(scores)):
	print(scores[i])

scores.reverse()

print("The contents after a reverse:")

for i in range(len(scores)):
	print(scores[i])
