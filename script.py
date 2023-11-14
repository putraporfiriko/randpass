import random

symbol = 0
lower = 0
upper = 0
number = 0
count = 0
password = []
pyperclip_installed = False

# pyperclip check. if exception, say copy feature is not available 
try:
    import pyperclip
    pyperclip_installed = True
except ImportError:    
    print("pyperclip module is not installed. Copy feature is not available. Please install pyperclip module using pip install pyperclip")

def copy_print():        
    if pyperclip_installed == True:
        copyconf = input("Do you want to copy the password to your clipboard? (Press enter for yes): ")
        copyconf = 'y' if copyconf == '' or copyconf.lower == 'y' else copyconf
        if copyconf == 'y':
            pyperclip.copy(''.join(password))
            print("Password copied to clipboard!")
        else:
            print("Password: " + ''.join(password))
    else:
        print("Password: " + ''.join(password))


length = input("Hey, welcome. How many character do you want in your password? (press enter for 8): ")
length = 8 if length == '' else int(length)

uppercase = input("Do you want uppercase characters in your password? (Press enter for yes): ")
uppercase = "y" if uppercase == '' or uppercase.lower == 'y' else uppercase

lowercase = input("Do you want lowercase characters in your password? (Press enter for yes): ")
lowercase = "y" if uppercase == '' or 'y' or 'Y' else lowercase

numbers = input("Do you want numbers in your password? (Press enter for yes): ")
numbers = 'y' if numbers == '' or numbers.lower == 'y' else numbers

symbols = input("Do you want symbols in your password? (Press enter for yes): ")
symbols = 'y' if symbols == '' or symbols.lower == 'y' else symbols

while count < length:
    rand = random.randint(0, 3)
    if rand == 0:
        if uppercase == 'y':
            upper += 1
            password.append(chr(random.randint(65, 91)))
            count += 1
    elif rand == 1:
        if lowercase == 'y':
            lower += 1
            password.append(chr(random.randint(97, 123)))
            count += 1
    elif rand == 2:
        if numbers == 'y':
            number += 1
            password.append(chr(random.randint(48, 58)))
            count += 1
    elif rand == 3:
        if symbols != 'y':
            r = random.randint(0, 2)
            symbol += 1
            if r == 0:
                password.append(chr(random.randint(33, 48)))
            elif r == 1:
                password.append(chr(random.randint(123, 126)))
            elif r == 2:
                password.append(chr(random.randint(91, 97)))

copy_print()

print(f"\n password length: {length}, uppercase: {upper}, lowercase: {lower}, numbers: {number}, symbols: {symbol}")


