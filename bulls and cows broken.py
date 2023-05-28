import random

# Generate 4 random numbers between 1 and 10
numbers = random.sample(range(1, 11), 4)

attempts = 0

# Prompt the user to enter 4 numbers between 1 and 10
input_numbers = input("Enter 4 numbers between 1 and 10: ")


while attempts < 10:
    # Reset the bulls and cows counts for each guess
    bulls = 0
    cows = 0

    # Convert the input to integers
    try:
        input_numbers = " ".join(str(num) for num in input_numbers)
        input_numbers = input_numbers.split()
        input_numbers = [int(num) for num in input_numbers]

    except ValueError:
        print("Please enter valid numbers between 1 and 10.")
    else:
        # Check if the user has entered 4 numbers
        if len(input_numbers) != 4:
            print("Please enter 4 numbers between 1 and 10.")
        # Check if the user has entered valid numbers
        elif not all(1 <= num <= 10 for num in input_numbers):
            print("Please enter valid numbers between 1 and 10.")
        else:
            # Check the user's guess
            for i in range(4):
                if input_numbers[i] == numbers[i]:
                    bulls += 1
                elif input_numbers[i] in numbers:
                    cows += 1

            # Print the bulls and cows counts
            print(f"{bulls} bulls, {cows} cows")

            # Check if the user has won
            if input_numbers == numbers:
                print("You win!")
                break

            # Increment the number of attempts
            attempts += 1
            continue

# Check if the user has lost
if attempts == 10:
    print("You lose.")