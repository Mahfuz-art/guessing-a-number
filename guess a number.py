secretnum = 7
num = int(input("Guess a number between 1 to 10"))
if secretnum<num :
    print("It is too high")
elif secretnum>num :
    print("It is too low")
elif secretnum==num :
    print("Congratulations! You guessed it right!")  
else :
    print("Error!")