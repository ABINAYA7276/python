x = 5 # when value is assign is called variable
y = "abi"
print(x)
print(y)

x = 4     # x is of type int
x = "abi" # x is now of type str
print(x)  #which one is enter in last that will be print in output"""

'''casting'''
x = str(3)    # x will be '3' in this case 3 will be consider as the string 
y = int(3)    # y will be 3     
z = float(3)  #in this case 3 will be consider as the string is called ''' 

x = 5
y = "sai"
print(type(x)) #in this type function show up the its is string or integer
print(type(y)) #get the type'''

x = "venkat"
# is the same as 
x = 'venkat' 

a = 4  #'''its is case sensitive  '''
A = "Sally" #we want sally but we call the func() is
'''A will not overwrite a '''# print(a) it"a error

'''variable name'''
#variable name have some rule except it case sensitive
myvar = "I"
my_var = "l"
_my_var = "U" 
myVar = "a" 
MYVAR = "b"
myvar2 = "i"
#illegal
'''2myvar = "o"
my-var = "k"  
my var = "k" '''#it is misbehave the rule
#double variable name
myVariableName = "John" '''it is except first one its capital''' # camel case
MyVariableName = "John" '''each word start with a capital letter''' #pascal case
my_variable_name ="abi"


x, y, z = "Orange", "Banana", "Cherry" #assign thr multiple value
print(x)
print(y)
print(z) #multiple value to multiple variable

x = y = z = "Orange"
print(x)
print(y)
print(z)  #assign multiple variable for single value

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)  #unpack the collection

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #first method , through this method is used to easily add
print(x + y + z ) #second method ,but different datatype is not adding using +
x="python is awesome"
print(x) #third method
