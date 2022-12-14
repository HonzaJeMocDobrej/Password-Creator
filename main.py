import string
import random

print("How long would you like your password? (chars) \n")
i1 = int(input())
print(' ')

def pas(i1):
    print("Would you like a special characters in your password?")
    print(' ')
    print("type yes / no \n")
    i2 = str(input())
        
    print(' ')
    print("Would you like a numbers in your password?")
    print(' ')
    print("type yes / no \n")
    i4 = str(input())
    
    print(' ')
    print("Would you like your password randomly uppercase?")
    print(' ')
    print("type yes / no \n")
    i5 = str(input())
    
    if i2 == "no" and i4 == "no" and i5 == "no":
        letters = string.ascii_lowercase
        finString1 = ''.join(random.choice(letters) for i in range(i1))
        print(' ')
        print("Your new password is: " + finString1)
        
    if i2 == "yes" and i4 == "no" and i5 == "no":
        print(' ')
        print("How many special characters would you like to have in your password? \n")
        i3 = int(input())
        print(' ')
        nochar = string.ascii_lowercase 
        char = string.punctuation
        chars1 = ''.join(random.choice(nochar) for i in range(i1-i3)) + ''.join(random.choice(char) for i in range(i3))
        finString1 = ''.join(random.sample(chars1, i1))
        print("Your new password is: " + finString1)
        
    elif i2 == "no" and i4 == "no" and i5 == "yes":
        nochar = string.ascii_letters 
        finString1 = ''.join(random.choice(nochar) for i in range(i1))
        print("Your new password is: " + finString1)
    
    elif i2 == "no" and i4 == "yes" and i5 == "no":
        print(' ')
        print("How many numbers would you like to have in your password? \n")
        i6 = int(input())
        nochar = string.ascii_lowercase 
        num = string.digits
        chars1 = ''.join(random.choice(nochar) for i in range(i1-i6)) + ''.join(random.choice(num) for i in range(i6))
        finString1 = ''.join(random.sample(chars1, i1))
        print("Your new password is: " + finString1)
        
    elif i2 == "no" and i4 == "yes" and i5 == "yes":
        print(' ')
        print("How many numbers would you like to have in your password? \n")
        i6 = int(input())
        nochar = string.ascii_letters 
        num = string.digits
        chars1 = ''.join(random.choice(nochar) for i in range(i1-i6)) + ''.join(random.choice(num) for i in range(i6))
        finString1 = ''.join(random.sample(chars1, i1))
        print("Your new password is: " + finString1)
        
    elif i2 == "yes" and i4 == "yes" and i5 == "no":
        print(' ')
        print("How many special characters would you like to have in your password? \n")
        i3 = int(input())
        print(' ')
        print("How many numbers would you like to have in your password? \n")
        i6 = int(input())
        print(' ')
        nochar = string.ascii_lowercase 
        char = string.punctuation
        num = string.digits
        chars1 = ''.join(random.choice(nochar) for i in range(i1-(i3+i6))) + ''.join(random.choice(char) for i in range(i3)) + ''.join(random.choice(num) for i in range(i6))
        finString1 = ''.join(random.sample(chars1, i1))
        print("Your new password is: " + finString1)
        
    elif i2 == "yes" and i4 == "no" and i5 == "yes":
        print(' ')
        print("How many special characters would you like to have in your password? \n")
        i3 = int(input())
        print(' ')
        nochar = string.ascii_letters 
        char = string.punctuation
        chars1 = ''.join(random.choice(nochar) for i in range(i1-i3)) + ''.join(random.choice(char) for i in range(i3))
        finString1 = ''.join(random.sample(chars1, i1))
        print("Your new password is: " + finString1)
        
    elif i2 == "yes" and i4 == "yes" and i5 == "yes":
        print(' ')
        print("How many special characters would you like to have in your password? \n")
        i3 = int(input())
        print(' ')
        print("How many numbers would you like to have in your password? \n")
        i6 = int(input())
        print(' ')
        nochar = string.ascii_letters 
        char = string.punctuation
        num = string.digits
        chars1 = ''.join(random.choice(nochar) for i in range(i1-(i3+i6))) + ''.join(random.choice(char) for i in range(i3)) + ''.join(random.choice(num) for i in range(i6))
        finString1 = ''.join(random.sample(chars1, i1))
        print("Your new password is: " + finString1)
            
pas(i1)

print(' ')
print("Made by: HONZA FEDOR")
