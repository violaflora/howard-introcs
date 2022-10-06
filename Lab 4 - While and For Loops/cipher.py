# An encoder/decoder for our spies to secretly send messages.
 
encryption_option = input("Would you like to Encode or Decode? ")
 
# should_encode will be true if the user
should_encode = "encode" in encryption_option.lower()
should_decode = "decode" in encryption_option.lower()
 
# Ask the user for their message and cipher number.
 
if should_encode:
   # Your code here!
   cipherNum = int(input("What is your cipher number? "))
   msg = input("What is your message? ")
   encodedMsg = ""
 
   for char in msg:
 
     next_char_index = ord(char) + cipherNum
 
     # given letter is capital wrap feature
     if ord(char) >= 65 and ord(char) <= 90:
       if next_char_index > 90:
         next_char_index = next_char_index - 26
     # given letter is lowercase wrap feature
     elif ord(char) >= 97 and ord(char) <= 122:
       if next_char_index > 122:
         next_char_index = next_char_index - 26
     elif ord(char) >= 32 and ord(char) <= 47:
       next_char_index = ord(char)
     else:
       pass
 
     encodedMsg += chr(next_char_index)
 
   print(encodedMsg)
  
elif should_decode:
   cipherNum = int(input("What is your cipher number? "))
   msg = input("What is your message? ")
   decodedMsg = ""
 
   for char in msg:
 
     next_char_index = ord(char) - cipherNum
 
     # given letter is capital wrap feature
     if ord(char) >= 39 and ord(char) <= 64:
       if next_char_index > 90:
         next_char_index = next_char_index + 26
     # given letter is lowercase wrap feature
     elif ord(char) >= 97 and ord(char) <= 122:
       if next_char_index > 122:
         next_char_index = next_char_index + 26
     elif ord(char) >= 32 and ord(char) <= 47:
       next_char_index = ord(char)
     else:
       pass
 
     decodedMsg += chr(next_char_index)
 
   print(decodedMsg)
else:
   # Print a nice notice that we only support encrypt/decrypt
   # Your code here!
   print("Sorry! We only support encrypt and decrypt.")