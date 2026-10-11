#
# price=100

#function ko define kiya hai 
def sum(a,b):
    print(a+b)

print(sum(1,2)) #function call



#clculate gst
def calc_gst(price):  #parameter
    new_price= price + price * 0.18
    print(new_price)
#function call
calc_gst(100)  #arguments
calc_gst(230)

# inbuilt function
print("hello")   
print(len([1,2,3,4,5]))
print(min([1,2,3,4,5]))
print(max([1,2,3,4,5]))


#module function
import math
print(dir(math))


#module
from math import sqrt
print(sqrt(16))

#module

from math import log2
print(log2(16))


#random function

import random 
print(random.randint(1,10))  #0 se 1 ke beech mein vaue generate kr ke dega