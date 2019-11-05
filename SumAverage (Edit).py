#Sum/Average Program
#Your first and last name: Bryan Le
#Your student ID: s1285204

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers (integers)
#Instead of searching for a name in the list
#   Compute the sum of all 20 numbers
#   Compute the average for all 20 numbers

#User interaction-
#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:

Number_list = []
tot = 0
for x in range(0,20):
    Numbers = input("Enter a number:")
    Number_list.append(Numbers)
for x in range(0,20):
    tot = tot + Number_list[x]
print('The sum of the number you entered is:' , sum(list))
print('The average of the numbers you entered is:' , (sum(list)/len(list)))




