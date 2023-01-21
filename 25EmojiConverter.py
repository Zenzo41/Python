message = input("Enter your message: ")
words = message.split() #default is whitespace by which the message is splitted

emojis = {
    ":)" : "😀",
    ":(" : "😕"
}
output = ''
for word in words:
   output += emojis.get(word,word)+" "
print(output)





