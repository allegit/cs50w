"""openFileHash.py

Reads a file containing scores then prints the data as-is, sorts and prints and then reverses
and prints. This program uses a hash to keep the names and score together
"""

scores = {}					# Hash to hold scores and names

result_f = open('results.txt')
for line in result_f:
	(name,score) = line.split()
	scores[score] = name

result_f.close()
print("The contents of the results file:")

for each_score in sorted(scores.keys(), reverse = True): 
	print('Surfer ' + scores[each_score] + ' scored ' + each_score)

