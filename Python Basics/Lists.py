#List is an ordered sequence of objects that can be any type.
li = [1,2,3,4,5]
li2 = ['a', 1, 'c']

#li3 = []
#li3[0] = 1
#These two lines above will make an error because arrays cannot be dynamically resized.

#What is a data structure?
#It's a way to organize information and data.
#So that these data structures can be used with different pros and cons.
#Like speed, memory, etc.
print(li[0])
#The square brackets allow us to contain information into a contained fashion.
#List Slicing similar to strings.
s = 'helloooo'
x = s[0:2:1] #start at index 0 end at 2 and go 1 by 1. 
print(x) #print out h and e
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
print(amazon_cart[0:2]) #prints notebooks and sunglasses
print(amazon_cart[0::2]) #The right is ignored and it'll just default to the end but what's important here is the fact that it will stepover two. So notebooks and toys will be printed out.
#List slicing essentially creates a new list.

#Strings are immutable, meaning that you can't change the text once it's created.
#Lists are however mutable. You can change the content of the list.
amazon_cart[0] = 'laptop'
print(amazon_cart)

new_cart = amazon_cart
#This isn't exactly simply copying it's passing a reference in memory.
#so if you change something in new cart it'll also change it in amazon cart.
#if you want to copy the array and assign it a different location in memory do this.
new_cart = amazon_cart[:] #This utilizes list slicing to it's advantage. start:end
#now if change an index of new cart, it won't change something in amazon cart.