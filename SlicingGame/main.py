'''
Purpose: Slicing Game Assignment 

Author: Saubaan Hasan
Creation Date: 05/29/2021
'''
# import statements
import random

# Variables
orig = "The Lazy fox"
totalCharacters=(len(orig)-1) #Checks the total character and subtracts 1 to find total amount of indexes
stepMax = 5 #Maximum number for the step value that can be generated
sliceMin = 3 #Minumum length required for the computer generated spliced characters. CAN BE CHANGED TO ANYTHING!
expected = "" #Initialized expected string
result = "" #Initialized result string

# Introduction and Sentence input
print("Welcome to the Slicing game, you will be given a phrase and you must figure out what the starting and ending indexes as well as the step value are using a sliced output")
print(" ")

# Prints the sentence that will be spliced
print("Sentence:", orig)

# Random slicing of original sentence & game startup
while len(expected) < sliceMin:
  originalStartIndex = random.randint(0,totalCharacters) #Chooses a random starting index
  originalEndIndex = random.randint(0,totalCharacters)   #Chooses a random ending index
  
  #Checks if the starting position and the ending position is the same. If so then it re-randomizes it
  while originalStartIndex == originalEndIndex:
    originalStartIndex = random.randint(0,totalCharacters)
    originalEndIndex = random.randint(0,totalCharacters)
    #Breaks out of the loop if the starting and ending index are different
    if originalStartIndex != originalEndIndex:
      break

  #Checks if the start index is smaller than the end index 
  if originalStartIndex < originalEndIndex:
    originalStepValue = random.randint(1,stepMax) #Makes the step value positive

  #Checks if the start index is greater than the end index 
  if originalStartIndex > originalEndIndex:
    originalStepValue = random.randint(1,stepMax)*-1 #Makes the step value negative

  expected = (orig[originalStartIndex:originalEndIndex:originalStepValue]) #Populates expected with the computer generated spliced characters

print ("Random Slice: ","|"+expected+"|")
print(" ")
#print ("Start: ",originalStartIndex, "End: ",originalEndIndex, "Step: ",originalStepValue)

#Checks if the user quess and the answer phrases match
while result != expected:
   startIndex = int(input("What is the Start Index? ")) #Asks user for the starting Index 
   endIndex = int(input("What is the End Index? ")) #Asks user for the ending Index 
   stepValue = int(input("What is the Step Value? ")) #Asks user for the step value 
   print(" ")

   result = (orig[startIndex:endIndex:stepValue]) #Populates result with the user inputted spliced characters
   print("Original: "+"|"+expected+"|","Your Input: "+"|"+result+"|")
   print(" ")

   #Checks if the user has found a matching spliced characters
   if result == expected:
     print("You Won, Congrats!")
     print(" ")

   #Try again message
   else:
     print("You Lost, Please try again!")
     print(" ")
     giveUp = input("Do you give up and want to see the answer? Please type Y for YES or N for NO: ")
     print(" ")

     if giveUp == "Y" or giveUp == "y":
       print("The Answer Was:")
       print("Start: ",originalStartIndex, "End: ",originalEndIndex, "Step: ",originalStepValue)
       break
     
     if giveUp == "N" or giveUp == "n":
       print("Alright then, Please try again!")
       print(" ")