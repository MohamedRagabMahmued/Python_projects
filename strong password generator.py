#import string module
import string
import random
#store all characters in lists (upper & lower case , digits , punctuations)
s1 = list(string.ascii_lowercase) #such as a,b,c,d,e,f
s2 = list(string.ascii_uppercase) #such as A,B,C,D,E,F
s3 = list(string.digits)          #such as 1,2,3,4,5,6
s4 = list(string.punctuation)     #such as _ , # , @ , .

# taket input from the user
chracters_number = input("how many characters for the password?: ")
# check the user input integer number from atlast 6 numbers
while True:
    try:
        chracters_number = int(chracters_number) 
        if chracters_number< 6:
            print("you need at lest 6 characters")
            chracters_number = input("pleas enter the unber again: ")
        else:
            break

    except:
        print("pleas enter numbers only")
        chracters_number = input("how many characters for the password?: ")

# shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
# colculate 30% and 20% of charcters
part1 = round(chracters_number * (30/100)) # round---> to mack digites
part2 = round(chracters_number * (20/100))

# creat password 60% leteers and 40% digits and punctuations
password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)

password = "".join(password[0:]) #بتحول الباسورد من لست الي استؤينج
print(password)