import random 

MAX_NUM = 50
MIN_NUM = 1
MIN_DEPOSIT = 1
MIN_STAKE = 1

LOW = 15
MEDIUM = 10
HIGH = 5


multiplier = {
    "low" : 2,
    "medium" : 4,
    "high": 10
}
def deposit():
    while True:
        amount = input(f"Enter the amount you want to deposit($) ")
        if amount.isdigit():
            amount = int(amount)
            if amount > MIN_DEPOSIT:
                return amount
            else:
                print(f"Enter amount greater than {MIN_DEPOSIT}")
        else:
            print("Enter a valid amount")

def user_stake(balance):
    while True:
        bet = input(f"How much do you want to stake($) ")
        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                if bet <= balance:
                    balance -= bet
                    return balance, bet
                else:
                    print("You dont have sufficient balance")
            else:
                print(f"Enter stake amount from {MIN_STAKE}$ above")
        else:
            print("Please enter a valid number")

def get_guess_limit():
    
    while True:
        level = input(f"Choose a difficulty level (low, medium, or high): ").lower()
        if level == 'low':
            return LOW
        elif level == 'medium':
            return MEDIUM
        elif level == "high":
            return HIGH
        else:
            print("Invalid input. Please choose: low, medium, or high.")

        
def generate_random_number():
    number_range = []

    for num in range(MIN_NUM,MAX_NUM + 1):
        number_range.append(num)
    
    return random.choice(number_range)

def check_user_input():
    while True:
        guess = input(f"Enter your guess from ({MIN_NUM} - {MAX_NUM}) ")
        if guess.isdigit():
            guess = int(guess)
            if MIN_NUM <= guess <= MAX_NUM:
                return guess
            else:
                print(f"Enter a number between {MIN_NUM} - {MAX_NUM}")
        else:
            print(f"Invalid Number, Please Enter a valid number between {MIN_NUM} - {MAX_NUM}")

    return guess

def play_game(limits, secret_number):
        for attempt in range(1, limits + 1):
            guess = check_user_input()
            if guess > secret_number:
                print(f"Your Guess is greater than the number ")
            elif guess < secret_number:
                print(f"Your Guess is less than the number ")
            elif guess == secret_number:
                print("Hooray You won!!!")
                return

        print(f"You Lost coz you already use all your attempt The correct number is {secret_number}")

        

def main():
    balance = deposit()
    new_balance, bet = user_stake(balance)
    number_to_guess = generate_random_number()
    limit = get_guess_limit()
    play_game(limit, number_to_guess)


