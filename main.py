import random

guessAttemptCount = 0
lowerBoundInt = input("Enter lower range: ")
lowerBoundInt = int(lowerBoundInt)
upperBoundInt = input("Enter upper range: ")
upperBoundInt = int(upperBoundInt)

randomNumber = random.randint(lowerBoundInt, upperBoundInt)

def numberGuessingLogic(attemptcount, highlowstr):
    if attemptcount < 3:
        print("The number is "+highlowstr+" than the guessed number! Try again!")
    elif attemptcount == 3:
        print("The number is "+highlowstr+" than the guessed number! LAST TRY!")
    else:
        print("GAME OVER! out of attempts")
        print("The number is "+str(randomNumber))
    return guessAttemptCount

while guessAttemptCount < 5:
    guessedNumber = input("Guess the number: ")
    guessedNumber = int(guessedNumber)

    if guessedNumber == randomNumber:
        print("Congratulations!! you guessed the number correctly!")
        print("I took you "+str(guessAttemptCount)+" attempt(s)")
        exit()
    elif guessedNumber > randomNumber:
        numberGuessingLogic(guessAttemptCount, "lower")
        guessAttemptCount = guessAttemptCount + 1
    elif guessedNumber < randomNumber:
        numberGuessingLogic(guessAttemptCount, "higher")
        guessAttemptCount = guessAttemptCount + 1


