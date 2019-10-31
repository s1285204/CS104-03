#Python Richter Scale Calculation
#Your first and last name: Bryan Le
#Your ID: s1285204

#Requirements Version 1:
# ask the user to 'Enter the Richter scale value: '
#   hint1: use an 'input' statement to input a variable called 'richter'
#   hint2: make sure 'richter' is a 'floating point' by using 'float'
# make sure richter scale value is greater than 0
#   if not, print "Value must be greater than 0"
# determine the Effect for the Richter scale value entered
#   hint1: use 'if' 'elif' and 'else' statements
#   hint2: remember to use ':' following all 'if' 'elif' and 'else' statements
# display or print the Effect
#   hint: use 'print' statement (only 1 effect should print)
# ask the user if they want to enter another richter scale value
#   if not, end the program

#Additional Requirements Version 2:
# ask the user to 'Enter the Richter scale value or -99 to end: '
#   if richter = -99, end the program

# make sure richter scale value is greater than 0
#   if not, print "Value must be greater than 0"
#   and make them enter another value


# Test your program several times with the following values:
#   8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6

scale = True
while scale == True:
    richter = float (input("richter scale value:"))
    print ("Enter value -99 to end program")
    if richter == -99:
        print ("End of program")
    if richter >= 8.0:
        print("Most Structures Fall")
    elif richter >= 7.0:
        print("Many Buildings Destroyed")
    elif richter >=6.0:
        print("Many Buildings Considerably Damaged, Some Collapse")
    elif richter >= 4.5:
        print("Damage to Poorly Constructed Buildings")
    elif richter <= 0:
        print("Value must be greater than 0! Enter a new value:")
    else:
        print("No Damage")
    

    

