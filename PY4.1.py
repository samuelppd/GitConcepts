"""sum=0
num=0
mean=0
text='#'
while text!='':
    text=input('Input an int : ')
    try:
        sum+=int(text)
        num+=1
    except ValueError:
        text=''
if num!=0:
    mean=sum/num
print(f'Mean : {mean}\n')"""

"""text=input('Liste de noms : ')
noms=text.split(' ')
if noms[0]!='':
    for nom in noms:
        print(f'Hi {nom}')
print()"""

"""nMax=int(input('Polynomial max degree : '))+1
polynomial=[]
for i in range(nMax):
    degree=int(input(f'x{i} : '))
    polynomial.append(degree)
x=int(input(f'x : '))
text=''
result=0
for i in range(nMax):
    temp=1
    for j in range(i):
        temp=temp*x
    result+=polynomial[i]*temp
    if i==0:
        text+=str(polynomial[i])
    else:
        text+=str(polynomial[i])+'x^'+str(i)
    if i<nMax-1:
        text+=' + '
print(f'{text} = {result}\n')"""

#functions (return something or none)
def hello():
    print('Hello World !')
hello()
print()

def add(a,b):
    c=a+b
    return c
print(f'{5}+{4}={add(5,4)}')
print()

def upp(string):
    return string.upper()
print(upp('helicoptere'))
print()

def func(a,b=5,c=10):
    print('a is ',a,' and b is ',b,' and c is ',c)
func(3,7)
func(25,c=24)
func(c=50,a=100)
print()

#def name(*arg,**kwarg):
# * pour une liste
# ** pour un dictionnaire