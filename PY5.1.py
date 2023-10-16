from ast import Name, Num
from tkinter import N


def my_function():
    print('Hello World')
my_function()

def my_function(name):
    print(f'Hello {name}')
my_function('Samuel')

def my_function(name,lastname):
    print(f'Hello {name} {lastname}')
my_function('Samuel','Poupardin')
my_function(lastname='Poupardin',name='Samuel')

# * si le nombre d'arguments est inconnu 
# par exemple pour les listes

def my_function(*kids):
    print(f'The youngest child is {kids[2]}')
my_function('Laure','Samuel','Solene')

# ** si pas savoir combien de keyword arguments
# par exemple pour les dictionnaires

def my_function(**kids):
    print(f"His lastname is {kids['lastname']}")
my_function(name='Samuel',lastname='Poupardin')

def my_function(x):
    return x*5
print(my_function(3))
print(my_function(5))
print(my_function(9))

def my_function():
    pass
my_function()

def my_function():
    print('Hello from a function')
my_function()

num1=72
num2=14
def my_function(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
print(f'The biggest of {num1} and {num2} is {my_function(num1,num2)}')

def my_function(*numbers):
    x=numbers[0]
    for i in numbers:
        if x<i:
           x=i
    return x
print(f'The biggest of the list is {my_function(9,2,5,10,1)}')

def my_function(*numbers):
    x=numbers[0]
    for i in numbers:
        if x>i:
           x=i
    return x
print(f'The smallest of the list is {my_function(9,2,5,10,1)}')

#try
try:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass

try:
    f=open('Document.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executed finally ...')

number=53
try:
    number%2
except Exception as e:
    print(e)
else:
    if number%2==0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')
finally:
    pass

while True: #while True mean while value error == True
    try:
        memory = input("Enter an int : ")
        number = int(memory)
        if number%2==0:
            print(f'{number} is even')
        else:
            print(f'{number} is odd')
        if number<0:
            print(f'{number} is negative')
        elif number==0:
            print(f'{number} is null')
        else:
            print(f'{number} is positive')
        prime=False
        if number>1:
            prime=True 
            for i in range(2,number):
                if number%i==0:
                    prime=False
        if prime==True:
            print(f'{number} is prime number')
        else:
            print(f'{number} is not prime number')
        break
    except ValueError as e:
        print(e)

