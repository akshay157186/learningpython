#Enter a String
a = input("Enter a String: ")
print('your first string value is {0}'.format(a))

#initialise a variable
i=0
print('the length of the entered value os {0}'.format(len(a)))


#print the characters in your string
while(i<len(a)):
    print (a[i])
    i=i+1

j=len(a) -1
while