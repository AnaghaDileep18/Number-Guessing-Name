import random
def game():
    print("..........................................NUMBER GUESSING GAME...........................................")
    print("This game has 3 levels of difficulty :\n 1. Easy \n 2. Medium \n 3. Hard")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        print("Difficulty level : Easy \n Number of guesses = Unlimited \n Number will be in the range of 1 - 30")
        n = random.randint(0,30)
        while(True):
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
    elif choice == 2:
        guess = 20
        n = random.randint(1,50)
        print("Difficulty level: Medium \n Number of guesses = 15 \n Number will be in the range of 1 - 50")
        for i in range(0,16):
            inp = int(input("Enter your guess = "))
            if inp<n:
                print("Try increasing the value")
                guess = guess -1
                print("Number of guesses left = ",guess)
                continue
            elif inp>n:
                print("Try decreasing the value")
                guess = guess - 1
                print("Number of guesses left = ", guess)
                continue
            else:
                print("Congratulations you guessed it right this time")
                print("The number of guesses you took to win the game = ",20 - guess)
                break
    elif choice == 3:
        print("Difficulty level: Hard \n Number of guesses = 10 \n Number will be in the range 1 - 100")
        n = random.randint(1, 100)
        guess = 10
        for i in range(0, 11):
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
            else:
                print("Congratulations you guessed it right this time")
                print("The number of guesses you took to win the game = ", 10 - guess)
                break
    else:
        print("Oops! Invalid choice. Please try again!")
        game()
game()