'''
Example to declare variables and scoping
'''

f=100
print(f)

'Re-initialize f'

f='CP4MCM'
print(f)

a="Guru"
b=95
print(a+str(b))

def someFunc():
    f = "This is python programming...."
    print(f)

someFunc()
print(f)

'Local variable scope can be changed to global'

def someFunc2():
    global f
    print(f)
    f = 'Python programming is fun...'

someFunc2()
print(f)
