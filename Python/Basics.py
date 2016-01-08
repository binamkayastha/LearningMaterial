Python
  Math/science
Dynamic
  Type “whatever”
Strongly typed
  Print(4+ “2”);
    Sends Type Error
MultiParadigm
  Object-Oriented
  Functional
  Procedural
  Whatever you want  (functions, methods)
Why python
  Easy to read:
    if a_list = []
Fast to write
import antigravity
import pygame
Python 2 vs Python 3
  Wiki.python.org/moin/Python2orPython3
Conditionals
If statements:
    look_like_this()

value = x if condition else y
LOOPS
while loops:
  stuff
for i in range(10):
  Do_thing


//"hello world"[5:]
//"reverse me" [::-1]
//x = []
//x.append(1)
//x + [2,3,4]
////tuple
/*
 *person = {
 *  'name' = "Ian"
 *  'favorite_food' = "cake"
 *}
 * & - combine
 * | - union
 * - - substract
 * 
 * List comprehension
 * set comprehension
 * def hello_world()
 *     print('hello, world')
 * 
 * 
 * closure
 *  You can define a function inside another function
 * 
 * tuples
 *  (12, 4, 21)
 *  Can't set can only get
 * enumerate - creates a list of things, giving a tuple.
 * for i, element in enumerate([])
 *     print("a{},b{}".format(i, element))
 * 
 * def drunk_print(*args):
 *    print('...'.join(args))
 * drunk_print("several arguments", '1', '2', '3');
 * 
 *anonymous functions, functions without a name.
 * *Zen of Python*
 *def __init__(self *given the explicit value of this*, initial_balance=0):
 *  self.balance = initial_balance=0
# * str(anything)
# *  def __str__(self, amount)
# *  class BankAcount(object)
# *  
# *  decorators
# *  generators
 #*  other fanciness
 #* */


def firstn(n):
  num = 0
  while num < n
      yield num
      num += 1

for num in firstn(10):
    print(num)

#
[2 ** n for n in range(10)] #generators
list(2 ** n for n in range(10))

#zip
names = ["ian", "potato"]
snakes = ["python", "boa", "black mamba"]
for i in range(2):
  print(names[i] + "'s favorite snake is " + snakes[i])

list(zip(names, snakes))
for name, snake in zip(names, snakes)
  print(name + "'s favorite snake is " + snake)

favorite_dishes = {'ian': 'potato'}

dict(list(zip(names, snakes)))

dict(['ian', 'potato'])
snake_lookup = zip(names, snakes)

#Multiple comparison operator
num = 42
40 < num and num <50
40 < num < 50

#slice operations
p = "potato salad"

p[0:5] = p[:5]
p[4:] #gives substring from 4 and on

ten = [0, 1,2, 3, 4, 5, 6, 7, 8, 9]
p[::]#multiple of for array
p[::-1] #backwards

#swap
a, b = b, a #swaps values of a and b
a, b, c = c, a, b #swaps values according

first, *last = [0,1,2,3]
#first become 0, *last become 1,2,3
first, *middle, last = [0,1,2,3]
#first becomes 0, *middle becoems 1,2, and last becomes 3

__exit__

#decorators
def my_decorator(f):
  def wrapped(*args, **kwargs):
    print("I'm wrapping the function f!")
    f(*args, **kwargs)
  return wrapped

@my_decorator       #Causes hello
def hello():
  print('hello')

hello()
 --> hello = my_decorator(hello)

 #Fib function with decoration
 results = {}
 def memoized(f):
  def wrappped(*args, **kwargs):
    if args in results:
      return results[args]
    else:
      ret = f(*args, **kwargs)
      results[args] = ret
      return ret
    return wrapped

  @memoized
  def fib(n):
    if n<=1:
      return n
    return fib(n-1) + fib(n-2)

  fib(30)


#Tuples again
#It's a datatype
a_thing = ('asdf', 'asdf', 1231)
a_thing[0]
a_thing[1]

a_thing[2] = 'asdf'

def foo(bar, baz, cow):
  print(bar + baz + cow)

foo('cows', 'go', 'moo')

phase = ('cows', 'go', 'moo')

foo(*phase)

def foo(*args):
  for argument in args:
    print(argument)

foo(1, 2, 3, 4, 5, 6, 7, 8)

foo(1, 2, 3, )



#FIZBUZZ
num = input()
def fizzbuzzFunction():
  if (int(num) % 15 == 0):
    return "FIZZBUZZ"
  elif (int(num) % 3 == 0):
    return "Fizz"
  elif (int(num) % 5 == 0):
    return "Buzz"
  else:
    return ""


/3
/5
/15 fixxbux

#Input
name = input()
