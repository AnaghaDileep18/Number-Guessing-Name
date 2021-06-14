import random
def decision():
    decide = input("Do you want to play again(yes/no) = ")
    if decide == 'yes':
        game()
    else:
        print("Goodbye...")
def game():
    print("..........................................NUMBER GUESSING GAME...........................................")
    print("This game has 3 levels of difficulty :\n 1. Easy \n 2. Medium \n 3. Hard")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        print("Difficulty level : Easy \nNumber of guesses = Unlimited \nNumber will be in the range of 1 - 30")
        n = random.randint(1, 30)
        while (True):
            inp = int(input("Enter your guess = "))
            if inp < n:
                print("Try increasing the value")
                continue
            elif inp > n:
                print("Try decreasing the value")
                continue
            else:
                print("Congratulations you guessed it right this time")
                break
        decision()
    elif choice == 2:
        print("Difficulty level: Medium \nNumber of guesses = 15 \nNumber will be in the range of 1 - 50")
        n = random.randint(1, 50)
        guess = 15
        x = False
        for i in range(1, 16):
            inp = int(input("Enter your guess = "))
            if inp < n:
                print("Try increasing the value")
                guess = guess - 1
                print("Number of guesses left = ", guess)
                continue
            elif inp > n:
                print("Try decreasing the value")
                guess = guess - 1
                print("Number of guesses left = ", guess)
                continue
            elif inp == n:
                print("Congratulations you guessed it right this time")
                print("The number of guesses you took to win the game = ", 15 - guess)
                x = True
                break
        if x == False:
            print("Oops! Game over.. The number you had to guess was = ", n)
        decision()

    elif choice == 3:
        print("Difficulty level: Hard \nNumber of guesses = 10 \nNumber will be in the range 1 - 100")
        n = random.randint(1, 100)
        guess = 10
        x = False
        for i in range(1, 11):
            inp = int(input("Enter your guess = "))
            if inp < n:
                print("Try increasing the value")
                guess = guess - 1
                print("Number of guesses left = ", guess)
                continue
            elif inp > n:
                print("Try decreasing the value")
                guess = guess - 1
                print("Number of guesses left = ", guess)
                continue
            elif inp == n:
                print("Congratulations you guessed it right this time")
                print("The number of guesses you took to win the game = ", 10 - guess)
                x = True
                break
        if x == False:
            print("Oops! Game over.. The number you had to guess was = ", n)
        decision()
    else:
        print("Oops! Invalid choice. Please try again!")
        game()
game()