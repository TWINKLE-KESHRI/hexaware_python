#Q1.Write a program to check whether a number entered is three digit number or not.

n = int(input('enter a number:'))
if len(str(n)) ==3:
     print("It's a three digit number")
else:
    print("Its not a three digit number")


#Q2. Write a program to check whether a person is eligible for voting or not.(voting age >=18)

age = int(input('enter your age:'))
if age>=18:
    print('You are Eligible for voting.')
else:
    print('You are under age')

#Q3 Write a program to check whether a person is senior citizen or not.
age = int(input('Please enter Your age: '))
if age>=65:
    print('You are a Senior citizen')
else:
    print('You are not a Sinor Citizen')

# Q4. Write a program to find the lowest number out of two numbers excepted from user.

a = int(input("Input first number:"))
b = int(input("Input second number:"))

print("The lowest number out of the two numbers you entered is {}".format(min(a,b)))

# Q5. Write a program to find the largest number out of two numbers excepted from user.

a = int(input("Input first number:"))
b = int(input("Input second number:"))

print("The largest number out of the two numbers you entered is {}".format(max(a,b)))

# Q6. Write a program to check whether a number (accepted from user) is positive or negative.

a = int(input("Please enter a number:"))

if a==0:
    print("Number is Zero")
elif a<0:
    print("The number you entered is a negative number.")
else:
    print("The number you entered is a positive number."


# Q7. Write a program to check whether a number is even or odd.
a = int(input("Please enter a number:"))

if a%2==0:
    print("{} is Even".format(a))
else:
    print("{} is odd".format(a))


# Q8. Write a program to display the spell of a digit accepted from user (like user input 0 and display ZERO and so on)
list_of_words=["Zero","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

num= int(input(print("Please enter a Digit:")))
print(list_of_words[num])


#Q9 Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

num = int(input("Please enter a number: "))

if num%6==0:
    print("{} is divisible by both 2 and 3".format(num))
else:
    print("{} is not divisible by both 2 and 3".format(num))


# Q10. Write a program to find the largest number out of three numbers excepted from user.

a = int(input("Input first number:"))
b = int(input("Input second number:"))
c = int(input("Input third number:"))
print("The largest number out of the three numbers you entered is {}".format(max(a,b, c)))

