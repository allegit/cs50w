# A Simple if else program sequence

first_names = ["Poorna", "Kartik", "Ritvik", "Vasanth"]

last_name = input()

if (last_name == 'Alle'):
    print('The family members could be:\ ')
    for i in first_names:
        print(i)
else:
    print('Doesn\'t belont to the Alle  Family')

print('Finally the length of Alle Family is: ')
print(len(first_names))