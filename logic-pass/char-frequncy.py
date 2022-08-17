# Q3/ write a function that count how many the given character repeated in a given string?

def char_frequncy(string,char):
    count = 0
    for i in string:
        if (i==char):
            count+=1
    return count  
# End function

# Testing                                                                        
string = input("Enter the string: ")                                            # myProjectt
char=input("Enter char to check frequncy: ")                                    # t

print("The letter ", char, "is repeated ",char_frequncy(string,char), "times")  # The letter  t is repeated  2 times
