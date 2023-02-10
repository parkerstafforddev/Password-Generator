import random




print("Hello! Thank you for using the password generator developed by Parker :)")

new = input("Please type 'gen' if you would like to create another password. Otherwise, type 'QUIT' to exit. ")

if new.lower() != 'quit':
    print("Generating new password")
    randint1 = random.randint(0,100)
    randint2 = random.randint(0,100)
    randint3 = random.randint(0,100)
    randint4 = random.randint(0,100)
    randint5 = random.randint(0,100)
    randint6 = random.randint(0,100)
    randint7 = random.randint(0,100)
    randint8 = random.randint(0,100)
    randint9 = random.randint(0,100)
    randint10 = random.randint(0,100)
    randint11 = random.randint(0,100)
    password = str(randint1) + str(randint2) + str(randint3) + str(randint4) + str(randint5) + str(randint6) + str(randint7) + str(randint8) + str(randint9) + str(randint10) + str(randint11)
    

    print("Your newly generated password is: " + password)
    input("Please hit ENTER to exit.")
    



    



