#Day_04 

print("\n ==== Number Guessing Game ====")

secret_num = 7
attempts = 0

while True:
    guess = int(input("Enter the secret Number (🤔): "))
    attempts += 1
    if guess == secret_num:
        print(f"\n Correct ☺ !, It took {attempts} attempts.")
        break
    print("\n Wrong guess ☹️ ,try agin")
