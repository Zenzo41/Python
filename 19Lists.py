# names = ['John','Bob','Sarah','Mary','Mosh']
# print(names[2]) #INDIVIDUAL VALUE ACCESSED

# print(names[2:]) #from 2nd index to the last

# print(names[1:3])# from 1 to 3rd index

# print(names)

# names[0] = 'Jon'

# print(names)


#Largest Number in a List
numbers = [1,2,3,4,5,6]
max = numbers[0]

for i in numbers:
    if i > max:
        max = i
print(max)