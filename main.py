import openai
import os

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

def start_game():
    print("Welcome to the Dynamic 'Suspect Loopholes' Game!")
    print("You are a detective, and your task is to find contradictions in the suspects' statements.")
    print("Let's begin...\n")

    statement = get_suspect_statement()
    print(f"Suspect's Statement: {statement}\n")

    options = generate_options(statement)
    print("Options:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choice = input("\nChoose the number of the loophole you want to point out: ")
    
    if choice.isdigit() and 1 <= int(choice) <= len(options):
        feedback = get_feedback(statement, options[int(choice) - 1])
        print(f"\nFeedback: {feedback}\n")
    else:
        print("\nInvalid choice. Please select a valid option number.\n")
        start_game()

# Start the game
start_game()
