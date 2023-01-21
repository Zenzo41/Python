# Dictionaries for storing key-value pair
# Eg: Name : John
# Email : john@gmail.com
# Phone: 1234

# keys must be unique ie we cant have two age keys

customer = {
    "name" : "John ",
    "age" : "30",
    "is_verified" : True
}

print(customer["name"])  # returns the value that is assigned with the key
# OR
print(customer.get("age"))


#adding key value pair

customer["birthdate"] = "Jan 1 1980"
print(customer.get("birthdate"))  #string inside the get method


#Enter phone number and display in word per letter

phone = input("Phone:")

numbers = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}
output = ""
for ch in phone:
    output += numbers.get(ch,"!")+" "  #get(ch,"!") ! as default value if no key-value pair
print(output)