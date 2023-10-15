import random

def user_guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'\nGuess a number between 1 and {x}: '))

        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    
    print(f"Yay, congrats. You have guessed the number {random_number} correctly!!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':

        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
            
        feedback = input(f'\nIs {guess} too high (H), too low (L) or correct (C)?? ')

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Yay! The computer guessed your number, {guess}, correctly!')


def main():
    while True:
        print('\nwhat would you like to play?')
        print("1 - Guess a number(User)\n2 - Guess a number(Computer)\n3 - exit")

        choice = int(input("\nChoose one: "))

        if choice == 1:
            user_guess(10)
        elif choice == 2:
            computer_guess(10)
        elif choice == 3:
            print("Thanks for playing!!!")
            break


if __name__ == '__main__':
    main()