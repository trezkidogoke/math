import random
import operator
import time

# Dictionary to map operators to their symbols and functions

operations = {
    ".",
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

# Function to generate a random 
def generate_problem():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(list(operations.keys()))

    # Ensure no division by zero
    if op == "/" and num2 == 0:
        num2 = 1

    return num1, op, num2

# Function to display and evaluate the problem
def solve_problem(num1, op, num2):
    answer = operations[op](num1, num2)
    return round(answer, 2)

# Main function to run the math challenge
def main():
    print("Math Challenge - Solve Simple Math Problems")
    score = 0

    for _ in range(5):  # Number of problems to solve
        num1, op, num2 = generate_problem()
        correct_answer = solve_problem(num1, op, num2)

        print(f"Solve: {num1} {op} {num2} = ?")
        try:
            user_answer = float(input("Your answer: "))
            if abs(user_answer - correct_answer) < 0.01:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nYour final score: {score}/5")

if __name__ == "__main__":
    main()
