def greet():
   return 'Hello Master Liam'
 
print(greet())
'''
Functions with parameters
'''
#def greet(name):
  # '''
  # Here are some comments/Greet that can be placed here\n  Ensure you use - help(greet) function
   #'''
   #return f"Hello there {name}, good Afternoon."
   
#print(greet('Felix'))
#print(greet('Coolio'))
#print(greet('Ryan'))

#help(greet)

'''
Arbitrary parameters - (tuple)
'''
#def fruits(*names):
  # '''
  # The star is a function that allows you to feed in more arguments or inputs (more then one fruit). It print each of the *names: The fruits. In tuples
  # '''
   #for fruits in names:
    # print(fruits)

#fruits("Orange, Pear, Bannana, Apple")
#fruits("Grape", "Pineapple", "Rasberry", "Blueberry")
# Quotations puts variables in a column each.
'''
Keyword parameters
'''
#def greet(name, msg):
  # '''
   #Keywords allow for convienient variables within a f string
   #'''
  # return f"Greetings {name}, {msg}"

#print(greet("Liam", "Good Afternoon!"))
#print(greet(name="Liam", msg="Afternoon matey! Rise and Shine."))
#print(greet(msg="Boom Boom Pow, dont waste your life to vainity", name="Master Bennett"))
'''
Arbitrary keywords - (type of dict)
'''
def person(**student):
   #print(type(student))
   #print(student)
   for key in student:
     print(student[key])

person(fname="Liam", lname="bizz", subject="python")

'''
Default parameter Values
'''
def greet(name="coolio"):
    return f"hello there with the famous name: {name}."

print(greet())
print(greet("dayana"))

'''
Pass statement
'''
def greet():
   pass

'''
recursion
'''
def factorial_recursive(n):
    if n == 1:
      return True
    else:
     return n * factorial_recursive(n -1)    

print(factorial_recursive(7))
#  Multiply a given number by every number less than it downt to 1 in a factorial way e.g if n is 5 then calculate 5*4*3*2*1 = 120 - n: is the highest starting number
