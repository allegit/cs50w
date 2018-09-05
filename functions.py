import math

def square(x):
    return x * x

def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))

if __name__ == "__main__":
    main()

"""
Learning functions
"""

def my_function():
    print("my_function")

def another_function(val):
    return val * 100

def repeat_print(s, times):
    print(s * times)

def hypotenuse(x,y):
    return math.sqrt(x ** 2 + y ** 2)

my_function()

a = another_function(4)
print('a: ' + str(a))

repeat_print('$', 5)

b = 5
print('hypotenuse: ' + str(hypotenuse(a,another_function(b))))
