#Palindrome Checker

string = input("Enter the value:")

reverse = string[::-1]

if(string==reverse):
    print("Yes it is a Palindrome")

else:
    print("No it is not a Palindrome")