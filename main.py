# Program to check if a number is prime or not
num = 67

# To take input from the user
# num = int(input("Enter a number: "))

# Define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # Check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # If factor is found, set flag to True
            flag = True
            # Break out of loop
            break

    # Check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
        
#Rayane et Snelson étape 6 changement


# CE CODE EST DANS UNE NOUVELLE BRANCHE !!!!!  