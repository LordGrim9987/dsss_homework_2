import random


def randfunc_randint(min, max):   #Generates a random integer between the given argument numbers- min and max
    """
    Random integer.
    """
    return random.randint(min, max)


def randfunc_randoperator():    #Selects a random arithmetic operator from the list ['+', '-', '*']
    """
    Random arithmetic operator from the list.  
    """
    return random.choice(['+', '-', '*'])


def func_eval_jumble(n1, n2, o):  #Returns the solution of the math problem and the problem itself, but jumbles the use of the operator
    """
    Takes the operator from the previous function as input along with two numbers and returns the problem and the solution after jumbling the 
    use of the operator.
    """
    p = f"{n1} {o} {n2}"    #Parses the output in the f-string format by taking the arguments of the function
    if o == '+': 
        a = n1 - n2
    elif o == '-': 
        a = n1 + n2
    else: 
        a = n1 * n2
    return p, a

def math_quiz():
    """
    The key function that runs the math quiz game. It generates random numbers and operators and asks the user to solve the math problems.
    And then solves the problem itself and compares the user's answer with the correct answer. 
    It keeps track of the score and displays the final score.
    """
    s = 0  # Initialize the score to 0
    t_q = 3  # Total number of questions

    print("Welcome to the Math Quiz Game!")  
    print("You will be presented with math problems, and you need to provide the correct answers.")  

    for _ in range(t_q):  # Loop through the number of questions
        n1 = randfunc_randint(1, 10)  # Generate first random number
        n2 = randfunc_randint(1, 5)  # Generate second random number
        o = randfunc_randoperator()  # Select the operator randomly

        PROBLEM, ANSWER = func_eval_jumble(n1, n2, o)  # Get the problem and the solution by invoking the functions
        print(f"\nQuestion: {PROBLEM}")  # Display the problem
        
        while True:
            useranswer = input("Your answer: ")  # Get the user's answer
            try:    # Try block to handle the exception if the user's input is not an integer
                useranswer = int(useranswer)  # Convert user's answer to integer
                break   # Break the loop if the user's answer is an integer
            except ValueError:
                print("Invalid input!! Please enter a valid integer.")  # Display error message if the user's input is not an integer

        if useranswer == ANSWER:  # Check if the answer is correct
            print("Correct! You earned a point.")  
            s += 1  # Increment score
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")  

    print(f"\nGame over! Your score is: {s}/{t_q}")  # Display final score

if __name__ == "__main__":  # Runs the math_quiz function only if the script is run directly
    math_quiz()
