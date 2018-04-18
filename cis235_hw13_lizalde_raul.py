# # Name: raul lizalde
# # CIS 235
# # Python Homework
#
# # Complete this assignment by editing this file replacing appropriate comments
# #  with your code. When you are complete, running this file should compute
# # with no errors and print the correct solutions to the stated problems.
#
import random		# This makes the random number functions available
import math
# # Problem 1
print("\n\nProblem 1 Solution:\n")
f = int(input("please enter first number: ")) #intitalizes variables as integers
s = int(input("please enter the second number: "))
t = int(input("please enter the third number: "))
n = 3 #number of inputs
sn = (f+s+t)#sum of input
avg = (sn // n)#avg of input
p = (f * s * t) #product of input
print ("the sum is: ", sn)
print ("the average is: ",avg)
print ("the product is: ", p)
##finds largest number
if f > s:
	print ("The largest number is ", f)
elif s > t:
	print("The largest number is ",s)
else:
	print ("The largest number is", t)
	##finds smallest number
if f < s:
	print ("The smallest number is ", f)
elif s < t:
	print("The smallest number is ",s)
else:
	print ("The smallest number is", t)
input("hit enter to continue")
# # # Problem 2

print("\n\nProblem 2 Solution:\n")

age = int(input ("please enter your age:")) # asks for age

if age < 2:
	print ("you are a baby") #checks if under 2
elif 2 <= age < 4:
	print ("you are a toddler") # checks if between 2 and 4
elif 4 <= age < 13:
	print ("you are an adolescent") # checks if between 4 and 13
elif 13 <= age < 20:
	print ("you are a teenager") # checks if between 13 and 20
elif 20 <= age < 65:
	print ("you are an adult") # checks if between 20 and 65
else:
	print ("you are an elder") # checks if over 65
input("hit enter to continue") #waits for user input to go to next problem
##Problem 3
print("\n\nProblem 3 Solution:\n")
list = ["number", "square", "cube"]
print ('\t'.join(list)) #prints the column names with tab spacing between
for x in range(0,11):
	print('{0:2d}\t {1:3d}\t {2:4d}'.format(x, x**2, x**3)) #creates list  and populates
input("hit enter to continue")
# Problem 4
print("\n\nProblem 4 Solution:\n")
list = ["n", "10*n", "100*n", "1000*n"] # names columns
n = int(input("please enter a number")) #asks for input
print ('\t '.join(list)) #prints column names before printing list
for x in range(1,n+1):
	print('{0:2d}\t {1:3d}\t {2:4d}\t {3:5d}'.format(x, x*10, x*100, x*1000)) #prints list and populates
input("hit enter to continue")


# Problem 5
print("\n\nProblem 5 Solution:\n")
x = random.randint(1,10) #chooses a random int between 1 and 10
guess = 0 #intitalizes guess
guesses = 0 #intitalizes guesses
while guess != x: #creates a loop where it runs so long as guess does not = x
	guess = int(input("Guess a number between 1 and 10: ")) #askes for users guess
	if guess != x: #checks against x
		print ("wrong try again")
	guesses += 1 #adds one to number of guesses if user gets it wrong
print ("Correct! The number was ",x)
print ("and you it took you", guesses," tries")
input("hit enter to continue")

# Problem 6
print("\n\nProblem 6 Solution:\n")
x = random.randint(1,10) #chooses a random int between 1 and 10
guess = 0 #intitalizes guess
guesses = 0 #intitalizes guesses
while guesses != 4: #creates a loop where it runs so long as guesses does not = 4
	guess = int(input("Guess a number between 1 and 10: ")) #askes for users guess
	if guess != x: #checks against x
		print ("wrong try again")
	guesses += 1 #adds one to number of guesses if user gets it wrong
	if guess == x: #if correct
		print ("Correct! The number was ",x)
		print ("and you it took you", guesses," tries")
		break #exits loop if correct
else: # if user excedes 4 tries then prints
	print("too many guesses! try again")

input("hit enter to continue") # waits for user to hit enter to exit program
