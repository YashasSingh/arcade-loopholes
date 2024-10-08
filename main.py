import openai
import os
import random
import time

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_suspect_statement(difficulty):
    """Generate a suspect's statement using OpenAI GPT based on difficulty level."""
    prompt = f"Create a {difficulty}-level suspect's statement for a crime scene with at least one logical loophole."
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

def generate_case_story(difficulty):
    """Generate a background story for the case based on the difficulty level."""
    prompt = f"Create a background story for a detective game case at {difficulty} difficulty. Include details about the crime scene, suspects, and potential motives."
    response = openai.Completion.create(
        model="text-davinci-004",
        prompt=prompt,
        max_tokens=200
    )
    story = response.choices[0].text.strip()
    return story

def analyze_clue(statement):
    """Allow players to analyze clues and gather more information."""
    prompt = f"Analyze this statement for hidden clues or evidence: '{statement}'. Provide insight that might help uncover the truth."
    response = openai.Completion.create(
        model="text-davinci-004",
        prompt=prompt,
        max_tokens=100
    )
    clue_analysis = response.choices[0].text.strip()
    return clue_analysis

def timed_input(prompt, timeout):
    """Function to handle timed input from the player."""
    print(prompt)
    start_time = time.time()
    input_value = ""
    while time.time() - start_time < timeout:
        if input_value:
            break
        input_value = input()
    if not input_value:
        print("\nTime's up!")
    return input_value

def manage_inventory(inventory, item):
    """Manage player's inventory by adding new evidence or clues."""
    inventory.append(item)
    print(f"\nNew evidence added to inventory: {item}")
    print(f"Current Inventory: {inventory}")

def start_multiplayer_game():
    print("Welcome to the Advanced Multiplayer 'Suspect Loopholes' Game!")
    print("You are detectives competing to solve cases by finding contradictions in suspects' statements.")

    # Select number of players
    player_count = int(input("Enter the number of players (2-4): "))
    while player_count < 2 or player_count > 4:
        player_count = int(input("Invalid number. Please enter a number between 2 and 4: "))

    players = [{"name": input(f"Enter player {i + 1}'s name: "), "score": 0, "inventory": []} for i in range(player_count)]

    # Select difficulty level
    difficulty = input("Choose difficulty level (easy/medium/hard): ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input("Invalid choice. Please choose difficulty level (easy/medium/hard): ").lower()

    # Generate a case story
    story = generate_case_story(difficulty)
    print(f"\nCase Background:\n{story}\n")
    print("Let's begin solving the case...\n")

    rounds = 3  # Number of suspects/statements to analyze
    timer = {"easy": 60, "medium": 45, "hard": 30}[difficulty]  # Set timer based on difficulty

    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}:\n")
        for player in players:
            print(f"{player['name']}'s turn:\n")
            statement = get_suspect_statement(difficulty)
            print(f"Suspect's Statement: {statement}\n")

            options = generate_options(statement)
            print("Options:")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")

            choice = timed_input(f"\nChoose the number of the loophole you want to point out (or type 'hint' for a hint, 'analyze' to analyze clues). You have {timer} seconds: ", timer)

            if choice.lower() == "hint":
                hint = get_hint(statement)
                print(f"\nHint: {hint}\n")
                choice = timed_input(f"\nNow, choose the number of the loophole you want to point out. You have {timer} seconds: ", timer)

            elif choice.lower() == "analyze":
                analysis = analyze_clue(statement)
                print(f"\nClue Analysis: {analysis}\n")
                manage_inventory(player['inventory'], analysis)
                choice = timed_input(f"\nNow, choose the number of the loophole you want to point out. You have {timer} seconds: ", timer)

            if choice.isdigit() and 1 <= int(choice) <= len(options):
                feedback = get_feedback(statement, options[int(choice) - 1])
                print(f"\nFeedback: {feedback}\n")
                if "Correct" in feedback:
                    player['score'] += 1
                    print(f"Well done, {player['name']}! Your score increases by 1.\n")
                else:
                    print("Incorrect choice. No points awarded.\n")
            else:
                print("\nInvalid choice or time ran out. Please select a valid option number.\n")

            print(f"Current Score for {player['name']}: {player['score']}\n")
    
    # Determine winner(s)
    max_score = max(player["score"] for player in players)
    winners = [player["name"] for player in players if player["score"] == max_score]
    if len(winners) > 1:
        print(f"It's a tie! The winners are: {', '.join(winners)} with a score of {max_score}.")
    else:
        print(f"The winner is {winners[0]} with a score of {max_score}!")

    display_leaderboard()
    replay_choice = input("Would you like to play again? (yes/no): ")
    if replay_choice.lower() == "yes":
        start_multiplayer_game()
    else:
        print("Thank you for playing! Goodbye!")

def save_score(score):
    """Save the player's score to the leaderboard."""
    with open("leaderboard.txt", "a") as f:
        player_name = input("Enter your name for the leaderboard: ")
        f.write(f"{player_name}: {score}\n")

def display_leaderboard():
    """Display the leaderboard with top scores."""
    print("\nLeaderboard:")
    try:
        with open("leaderboard.txt", "r") as f:
            scores = [line.strip() for line in f.readlines()]
            scores.sort(key=lambda x: int(x.split(": ")[1]), reverse=True)
            for rank, score in enumerate(scores[:5], 1):
                print(f"{rank}. {score}")
    except FileNotFoundError:
        print("No leaderboard data found.")

# Start the multiplayer game
start_multiplayer_game()
