#Functions are stuff like len() which you call by name.
#Here we discuss methods. Which are for objects. An action owned by something.

basket = [1,2,3,4,5]
print("This section is about adding things to a list.")
#adding 
new_list = basket.append(100) #Appends an object to the end of the list. In python everything is an object.
print(basket)
print(new_list)
#Output for newlist is none and 100 is appended to the basket.
#That new list is none and this is because append changes the list in place. It does not return a value.

newlist = basket.copy() #This creates a copy of basket instead of a reference to basket in memory.
print(newlist)
newlist[5] = 6
print(basket)
print(newlist)

basket.extend([100, 'a'])# adds the specified list elements (or any iterable) to the end of the current list.
#Iterable is an object which can be looped over or iterated over with the help of a for loop. 
#Objects like lists, tuples, sets, dictionaries, strings, etc. are called iterables. In short and simpler terms, iterable is anything that you can loop over.
#There is also an insert method which is like so, basket.insert(4,100). Self explanatory.
print(basket)

#Removing methods
print("Methods for removing from list.")
x = basket.pop() #returns the index that was removed
print(str(x) + " was removed")  #If you specify an index, the return value will be that index.
#removing contents from an array in java: https://stackabuse.com/remove-element-from-an-array-in-java/
print(basket)
#There is also a remove method that will remove the value given. Remove deletes the first occurance of the value.
#Clear() gets rid of all the contents inside the array.
basket.clear() #clear makes the array size 0
print(len(basket))
print(basket)