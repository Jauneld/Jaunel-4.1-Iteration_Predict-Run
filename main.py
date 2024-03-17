#Jaunel Deans
#November 2, 2023
# We are writing a prediction of what it will do when it runs.

## Example code 1

print("What is the capital of France?")#The print function will be used to print the question to the user. The question is "What is the capital of France?"(Out of the loop)
answer = input() #Define a variable named answer. The value the user inputted will be assigned to answer (Out of the loop)

while answer != "Paris":#creates a while loop that says if the value of answer is not equal to Paris, then the loop will run.(Out of the loop)
  print("Incorrect! Try again.")#If the condition in the while loop is met, then the print function will print "Incorrect! Try again." (Inside the loop)
  answer = input("What is the capital of France?")#The value of answer will be assigned to the input function. The question is "What is the capital of France".(Inside the loop)

print("Correct!")#If the while loop is false, the print function will print "Correct!". This out of the loop 

## Example code 2

counter = 1 #Define a variable named counter. The value 1 will be assigned to counter.(Out of the loop)

while counter < 5:#Creates a while loop that says if the value of counter is less than 5, then the loop will run.(Out of the loop)
  print("This code is inside the loop")#If the condition in the while loop is met, then the print function will print "This code is inside the loop(Inside the loop)
  counter += 1#Then the value of counter will be incremented by 1.(Inside the loop)

#After the loop becomes false nothing will print
#Also the loop will run 4 times because the value of counter is incremented by 1 each time. It will print out "This code is inside the loop" 4 times.