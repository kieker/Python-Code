def HelloWorld(name):
    print('Hello ' + name)

'''
name = input("What is your name?")
HelloWorld(name)
'''

def addNumbers(num1,num2):
    try:
        newnum = int(num1) + int(num2)
        print(newnum)
    except:
        print('The number you entered was invalid')

num1 = input("What is the first number:")
num2 = input("What is the second number:")
addNumbers(num1,num2)
