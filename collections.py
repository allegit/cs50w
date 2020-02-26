'''
This python snippet 
'''

def convertToStr(input_list, separator):
    # Join all the elements in the list into a string
    final_str = separator.join(input_list)
    return final_str

separator = ', '
alist = ["apple", "banana", "cherry", "orange", "kiwi", "watermelon", "strawberry", "pineapple"]
print(alist)
print('The second fruit in the list is: ' + convertToStr(alist[1], separator))
print('The last fruit in the list is: ' + convertToStr(alist[-1], separator))
print('The second, third and fourth fruits from the list are: ' + convertToStr(alist[2:5], separator))
print('The first four fruits from the list are: ' + convertToStr(alist[:4], separator))
