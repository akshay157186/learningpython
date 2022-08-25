#Enter a String
a = input("Enter a String: ")
print('your first string value is {0}'.format(a))
print(f"Print characters of {a} in reverse")

#print the characters in your string
for i in range(len(a)-1,-1,-1):
    print(a[i])