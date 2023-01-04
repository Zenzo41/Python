# Display from (0,0) to (3,2):

for x in range(4):  #number from 0 to 3
    for y in range(3):   #number from 0 to 2
        print(f'({x} , {y})')
        
#Display the following pattern using nested loop:
#   xxxxx
#   xx
#   xxxxx
#   xx
#   xx

number = [5,2,5,2,2]
# Cheat way:

for num_count in number:
    print ('x' * num_count)
    
# Desired Way:
    
print("Desired Way:")
for x_count in number:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
    