#Create a dictionary and take input from user and return the meaning of that word.
#d={"set":"Collection of objects","noun":"Name of anything","mutable":"Changable","immutable":"Unchangeable"}
#x=input("Write the word to find meaning of that word: ")
#print("The meaning of",x ,"is: ",d.get(x))

l=[1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e","f","g"]
for i in l:
   if str(i).isnumeric() and i>6:
      print(i)