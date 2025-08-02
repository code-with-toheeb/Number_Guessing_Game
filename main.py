import random 

MAX_NUM = 50
MIN_NUM = 1
def computer_pick():
    number_list = []

    for num in range(MIN_NUM,MAX_NUM + 1):
        number_list.append(num)
    
    c_pick = random.choice(number_list)

    return c_pick


def user_pick(generated_number):
    while True:
        user_guess = input(f"Enter your guess from ({MIN_NUM} - {MAX_NUM}) ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
            if MIN_NUM <= user_guess <= MAX_NUM:
                if user_guess > generated_number:
                    print(f"Your Guess is greater than the number ")
                elif user_guess < generated_number:
                    print(f"Your Guess is less than the number ")
                elif user_guess == generated_number:
                    print("Hooray You won!!!")
                    break
        else:
            print(f"Please enter a valid number ")
    

def main():
    machine_pick = computer_pick()
    while True:
        user_pick(machine_pick)
        break

main()