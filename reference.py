

# S Y N T A C T I C A L   C O N V E N T I O N S

# typical naming convention is to use snake_case with lower case characters
# for everything except for Classes and boolean True/False

# the body of each function, loop, Class, etc is distinguishable 
# through the use of strict indentation


# P R I M I T I V E   T Y P E S 

# integers
# 1, 3, 21
print(type(5))

# floats
# 3.1, 1.76, .04
print(type(3.14159))

# strings
# 'Ayy lmao'
print(type('Ayy lmao'))

# strings are indexed as arrays and can be easily manipulated
my_string = 'Ayy lmao'


# S T R I N G   M A N I P U L A T I O N 
# a lot of string manipulations can be performed with brackets

# returns character at index of 2
print(my_string[2]) 

# slice at indices
print(my_string[1:7])

# out of range indices only return values that are present
print(my_string[0:99])

# negative values wrap such that...
print(my_string[-4])

# ...to access last value, you can always reference the -1 index
print(my_string[-1])

# len() returns length of string
print(len(my_string))


# F U N C T I O N S

# def is for function definitions.  The body of a function is identified by its Indentation
def greet():
  print('Aloha')

greet()

# printing a function without parentheses returns its address in memory
# this address appears to change everytime the script is ran
print(greet)

# similar to Javascript, everything is an object, including functions
# and as such, they can be assigned to, and invoked by, variables
Aloha = greet
Aloha()

# functions take arguments and return values
def double(x):
  return x * 2

double(3)

# note the difference in behavior with function return values and functions that don'try
three_doubled = double(3)

print(three_doubled) #prints 6
print(greet) #prints address in memory

# VARIABLE SCOPE is restricted to body of function it is defined within
def multiply(a, b):
  result = a * b
  return result

#print(result) #will generate an undefined error


# B O O L E A N   O P E R A T I O N S     

print( 1 > 0 )
print( 1 < 0 )
print( 1 >= 0 )
print( 1 <= 0 )
print( 1 == 1 )
print( 1 == 0 )
print( 1 != 0 )
print( 1 != 1 )

# STRING COMPARISON is very interesting and performed character-by-character
# and is determined by alphabetical order such that 'a' is a lower value than 'b'

print('a' > 'b') #false
print('a' < 'b') #true

# in lengthier strings, the evaluation occurs where the first value mismatch occurs
print('aaaab' > 'az') #false

# if there are no value mismatches between any two individual characters, the strings
# length comes into play somehow (not sure)
print('aaaaa' == 'a') #false


# C O N D I T I O N A L   S T A T E M E N T S

# IF:ELSE is pretty standard stuff
def check_temp(temp):
  if temp > 80:
    print("It's hot!")
  else:
    print("It's cool.")

check_temp(90)
check_temp(70)

# WHILE LOOPS
i = 0
while i < 10:
  print(i)
  i += 1  #oddly, the unary ++ operator does not work in python

# for loops in python are unique in that they are used to step through
# either characters of a string, or a range of numbers using the 
# range() function
for char in 'hello':
  print(char)

for num in range(10):
  print(num)


# D A T A   S T R U C T U R E S     

# LISTS (arrays, basically)
colors = ['red', 'yellow', 'blue']
print(colors)

colors.append('green') #adds one value to list
print(colors)

colors.extend(['orange', 'violet']) #adds another list to list
print(colors)

colors.remove('yellow') #removes first instance of specified value
print(colors)

colors.pop() #removes last value of list and returns its value
print(colors)

# SETS are non-repeating groupings of data, much like lists
days = {'mon', 'tue', 'wed', 'thu', 'fri'}
colors = {'red', 'red', 'yellow', 'blue'} #works, but only prints out one red.
                                          #the duplicate is discarded

# the 'in' keyword can be used to check if a value is already a set
print('mon' in days) #true

days.add('sat') #adds an entry

#DICTIONARIES are groupings of key-value pairs
grades = { 'Sally': 88, 'Henry': 89 }

#key-value pairs can be added using bracket notation
grades['Bodiddly'] = 47

#del keyword removes values based on key
del grades['Sally']


# C L A S S E S   A N D   O O P    

# def __init__ is a required constructor that is called upon instantiation
class Animal:
  def __init__(self, habitat, diet):
    self.habitat=habitat
    self.diet=diet
  def speak(self):
    print(f"I live in the {self.habitat} and eat {self.diet}.")

# the following demonstrates inheritance from Animal class
class Lion(Animal):
  def __init__(self, pride_size, title):
    super().__init__ ('savanah', 'meat')  # super() adds parent class __init__ traits
    self.pride_size=pride_size
    self.title=title
  def roar(self):
    print(f"I'm the {self.title} of a pride of {self.pride_size}. ROAR!")

my_lion = Lion(12, 'King')

my_lion.speak()
my_lion.roar()

