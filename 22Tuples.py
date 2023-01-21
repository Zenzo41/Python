#Tuples are immutable ie we cant change them
numbers = (1,2,3,2,1,1,2,2,1)

# has only two methods. doesnt have methods like apppend,remove etc.
print(numbers.count(1)) # counts the no of times the number is repeated
print(numbers.index(2)) #returns the first instance of the given value

# numbers[0] = 22  this doesnt work as tuple doesnt support assignment
