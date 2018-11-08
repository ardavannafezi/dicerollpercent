import random
import time

min = 1
max = 6
b=1
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0


print("0x007\ncoded by ardavan\n\n")
print("how many throw do u want??\n")
a = int(input())
print("\ngetting ready\n")
time.sleep(0.2)
print("\n=====")
time.sleep(0.2)
print("\n=====***--***======")




while b < a:
    num = random.randint(min, max)
    b += 1
    print(num)
    time.sleep(.001)
    if num == 1:
       one += 1
    elif num == 2:
       two += 1 
    elif num == 3:
       three += 1  
    elif num == 4:
       four += 1  
    elif num == 5:
       five += 1  
    elif num == 6:
       six += 1   

print("\n---------------TIMES--------------\n")
time.sleep(1)    
print("number one = " + str(one))
print("number two = " +  str(two))
print("number three = " +  str(three))
print("number four = " +  str(four))
print("number five = " +  str(five))
print("number six = " +  str(six))
print("\n\n==============================")
time.sleep(1)   
print("\n---------------percents--------------\n")    
print("number one = " + str(one/a*100)+ "%")
print("number two = " +  str(two/a*100)+ "%")
print("number three = " +  str(three/a*100)+ "%")
print("number four = " +  str(four/a*100)+ "%")
print("number five = " +  str(five/a*100)+ "%")
print("number six = " +  str(six/a*100)+"%")




input()
      