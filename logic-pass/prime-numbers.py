# Q2/ Write a program to find all prime numbers up to a given range of numbers?

startRange = int (input("Enter a number for starting range: ")) 
endRange = int (input("Enter a number for end range: ")) 

print ("Prime numbers in the range", startRange, "to", endRange) 
for i in range(startRange, endRange+1): 
    flag = False 
    for j in range(2, i): 
        if (i % j == 0): 
            flag = True
            break 
        
    if (flag == False): 
        print (i)
