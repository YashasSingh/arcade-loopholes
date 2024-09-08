
# Advanced Multiplayer Dynamic Suspect Loopholes Game
![image](https://github.com/user-attachments/assets/b945d86a-cf22-4089-b10a-aedfa6f5f9c4)

Welcome to the **Advanced Multiplayer Dynamic Suspect Loopholes Game**! This is an interactive text-based detective game where players compete to solve cases by identifying logical loopholes in suspects' statements. 

## Game Overview

In this game, you and your friends take on the roles of detectives trying to uncover the truth behind various cases. Each round, you'll be presented with a suspect's statement that contains a logical contradiction. Your goal is to find the loophole by choosing the correct option from multiple choices. As you progress, you can gather clues, analyze evidence, and manage an inventory to help you solve the case.

## Features

- **Multiplayer Mode**: Supports 2-4 players competing to solve cases.
- **Dynamic Case Generation**: Each game includes a unique storyline with different suspects and statements.
- **Player Actions**: Players can ask for hints, analyze clues, and manage their inventory to make strategic decisions.
- **Multiple Difficulty Levels**: Choose from easy, medium, or hard to match your skill level.
- **Timed Rounds**: Each player has a limited amount of time to make their choice, adding an element of pressure.
- **Leaderboard**: Save and view the top scores to see who is the best detective!

## Installation

1. **Clone the Repository**: 
    ```bash
    git clone https://github.com/your-username/suspect-loopholes-game.git
    cd suspect-loopholes-game
    ```

2. **Install Required Packages**:
   Make sure you have Python 3.x installed. Install required dependencies using pip:

   ```bash
   pip install openai
   ```

3. **Set Up OpenAI API Key**:
   Obtain an OpenAI API key from [OpenAI](https://beta.openai.com/signup/). Set your API key as an environment variable:
   
   **On Windows**:
   ```bash
   set OPENAI_API_KEY=your_openai_api_key
   ```

   **On macOS/Linux**:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key
   ```

## How to Play

1. **Start the Game**:
   Run the script using Python:

   ```bash
   python suspect_loopholes_game.py
   ```

2. **Choose Number of Players**: 
   Enter the number of players (2-4) to begin.

3. **Select Difficulty Level**: 
   Choose a difficulty level (easy, medium, or hard).

4. **Read the Case Background**: 
   A unique story will be generated for each game, setting the context for the case.

5. **Analyze Suspect Statements**:
   Each round, a suspect's statement will be presented. Review the statement and use your detective skills to find the logical loophole.

6. **Make Your Choice**:
   Choose the correct option from the provided choices. You can ask for hints, analyze clues, or manage your inventory to improve your chances.

7. **Score Points and Compete**:
   Correct answers will earn you points. Compete against other players to become the top detective!

8. **End of Game**:
   After 3 rounds, the player(s) with the highest score wins. Scores are saved to the leaderboard.

## Contributing

Contributions are welcome! Please feel free to submit issues, fork the repository, and send pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

