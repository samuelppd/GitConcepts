#creating empty dictionary
from random import sample
from turtle import st


Dict={}
print(Dict)

#creating a dictionary
country_capitals = {
    "United States":"Washington D.C.",
    "Italy":"Naples",
    "England":"London"}
#1stValue=key, 2ndValue=value
#England=key, London=value

#printing the dictionary
print(country_capitals)

# /!\ list is mutable
# /!\ keys of dictionary are imutable, values are mutable

#change and add and delete a value
country_capitals["Italy"]="Rome"
print(country_capitals)
country_capitals["Germany"]="Berlin"
print(country_capitals)
del(country_capitals["United States"])
print(country_capitals)

print(country_capitals.keys())
print(country_capitals.values())
#propriete .get[key]
print(country_capitals.get("Italy")) 
#propriete popitem
#print(country_capitals[2]) FAUX
for country in country_capitals:
    print(country)
    capital=country_capitals[country]
    print(capital)
for keys,values in country_capitals.items():
    print(keys)
    print(values)

my_dict={1:"Hello",(1,2):"Hello Hi"}
print(my_dict)
print(1 in my_dict) #true
print("Hello" not in my_dict) #true
print("Hello" in my_dict) #false

#length
print(f"number of capitals : {len(country_capitals)}")

#nested dictionary
Dict={1:'Geek',2:'For',3:{'A':'Welcome','B':'To','C':'Geeks'}}
print(Dict)
print(Dict[3])
print(Dict[3]['A'])

Dict2=Dict.copy()
Dict2.clear()
print(Dict2)

#list #ordered, changeable, allow duplicate members
#tuple #ordered, unchangeable, allow duplicate members
#set #unordered, unchangeable, no duplicate members
#dictionary ##ordered, changeable, no duplicate members

cities=('Paris','Athens','Madrid')
mydictionary=dict.fromkeys(cities)
print(mydictionary)

continent='Europe'
mydictionary=dict.fromkeys(cities,continent)
print(mydictionary)

keys=['Ten','Tweny','Thirty']
values=[10,20,30]
num_dict=dict(zip(keys,values)) # zip pour creer des tuples
#num_dict=dict.fromkeys(keys,values) #marche pas, il faut utiliser zip
print(num_dict)

dict1={'Ten': 10, 'Tweny': 20, 'Thirty': 30}
print(dict1)
dict2={'Thirty': 30, 'Fourty': 40, 'Fiftyy': 50}
print(dict2)
#dict1.update(dict2)
#print(dict1)
dict3={**dict1,**dict2}
print(dict3)

sample_dict={'a':100,'b':200,'c':300}   
if 200 in sample_dict.values():
    print('200 present in a dict')
    
sample_dict={'emp1':{'name':'John','salary':7500},'emp2':{'name':'Emma','salary':8000},'emp3':{'name':'Brad','salary':500}}
print(sample_dict)
sample_dict.update
sample_dict['emp3']['salary']=8500
print(sample_dict)

#probleme dictionary
elements={'H':{'Element':'Hydrogen','AtomicNumber':1,'MeltingPoint':14,'BoilingPoint':20},
'He':{'Element':'Helium','AtomicNumber':2,'MeltingPoint':1,'BoilingPoint':4},
'Li':{'Element':'Lithium','AtomicNumber':3,'MeltingPoint':453,'BoilingPoint':1603},
'Be':{'Element':'Beryllium','AtomicNumber':4,'MeltingPoint':1560,'BoilingPoint':2742},
'B':{'Element':'Boron','AtomicNumber':5,'MeltingPoint':2349,'BoilingPoint':4200},
'C':{'Element':'Carbon','AtomicNumber':6,'MeltingPoint':3915,'BoilingPoint':3915},
'N':{'Element':'Nitrogen','AtomicNumber':7,'MeltingPoint':63,'BoilingPoint':77},
'O':{'Element':'Oxygen','AtomicNumber':8,'MeltingPoint':54,'BoilingPoint':90},
'F':{'Element':'Fluorine','AtomicNumber':9,'MeltingPoint':53,'BoilingPoint':85},
'Ne':{'Element':'Neon','AtomicNumber':10,'MeltingPoint':25,'BoilingPoint':27}}
element=input('Entrer un element : ')
temperature=int(input('Entrer une temperature : '))
if temperature<elements[element]['MeltingPoint']:
    state='solid'
elif temperature<elements[element]['BoilingPoint']:
    state='liquid'
else:
    state='gaz'
print(f'The element {element} is {state} at {temperature}K.')

