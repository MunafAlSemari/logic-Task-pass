# Q1/ Write a method that will remove any given character from a String ?

def remove_char(str,cha):
    newStr = filter(lambda x: x!= cha.lower() and x != cha.upper(), str)
    return "".join(newStr)
    #End method

#Testing
str=input("Enter the string: ")       # myProjectk
cha=input("Enter char to replace: ")  # k
print(remove_char(str,cha))           # myProject
