import openai
import os
import random

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_suspect_statement():
    """Generate a suspect's statement using OpenAI GPT."""
    prompt = "Create a suspect's statement for a crime scene with at least one logical loophole."
    response = openai.Completion.create(
        model="text-davinci-004",
        prompt=prompt,
        max_tokens=150
    )
    statement = response.choices[0].text.strip()
    return statement

def generate_options(statement):
    """Generate options to find the loophole in the suspect's statement using GPT."""
    prompt = f"Given the suspect's statement: '{statement}', provide three multiple-choice options to identify the logical loophole."
    response = openai.Completion.create(
        model="text-davinci-004",
        prompt=prompt,
        max_tokens=150
    )
    options = response.choices[0].text.strip().split('\n')
    return options

def get_feedback(statement, choice):
    """Get feedback on the player's choice using GPT."""
    prompt = f"Given the suspect's statement: '{statement}' and the player's choice: '{choice}', provide feedback on whether the choice identifies the loophole correctly."
    response = openai.Completion.create(
        model="text-davinci-004",
        prompt=prompt,
        max_tokens=150
    )
    feedback = response.choices[0].text.strip()
    return feedback

def get_hint(statement):
    """Get a hint for the suspect's statement using GPT."""
    prompt = f"Provide a hint to identify the logical loophole in the suspect's statement: '{statement}'."
    response = openai.Completion.create(
        model="text-davinci-004",
        prompt=prompt,
        max_tokens=100
    )
    hint = response.choices[0].text.strip()
    return hint

def start_game():
    print("Welcome to the Enhanced 'Suspect Loopholes' Game!")
    print("You are a detective, and your task is to find contradictions in the suspects' statements.")
    print("Let's begin...\n")

    score = 0
    rounds = 3  # Number of suspects/statements to analyze

    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}:\n")
        statement = get_suspect_statement()
        print(f"Suspect's Statement: {statement}\n")

        options = generate_options(statement)
        print("Options:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        choice = input("\nChoose the number of the loophole you want to point out (or type 'hint' for a hint): ")

        if choice.lower() == "hint":
            hint = get_hint(statement)
            print(f"\nHint: {hint}\n")
            choice = input("\nNow, choose the number of the loophole you want to point out: ")

        if choice.isdigit() and 1 <= int(choice) <= len(options):
            feedback = get_feedback(statement, options[int(choice) - 1])
            print(f"\nFeedback: {feedback}\n")
            if "Correct" in feedback:
                score += 1
                print("Well done! Your score increases by 1.\n")
            else:
                print("Incorrect choice. No points awarded.\n")
        else:
            print("\nInvalid choice. Please select a valid option number.\n")
        
        print(f"Current Score: {score}\n")

    print(f"Game Over! Your final score is: {score}/{rounds}")
    replay_choice = input("Would you like to play again? (yes/no): ")
    if replay_choice.lower() == "yes":
        start_game()
    else:
        print("Thank you for playing! Goodbye!")

# Start the game
start_game()
