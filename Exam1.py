## Code for deciding which payment option is better for the employee

option1 = 100
option2 = 1

option1 = option1 * 10 

for i in range(10):
    option2 =+ option2 * 2

option2 = option2 - 1

if (option2<option1): 
    print("Option 1 is better")

if (option2>option1): 
    print("Option 2 is better")

if (option1 == option2):
    print("Option 1 and Option 2 pays the same")
