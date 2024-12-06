Detective Mystery Game: Catch the Robber

Welcome to the "Catch the Robber" interactive detective game, where you will use predictive analytics and data exploration to catch a robber based on clues provided in a dataset. This game is built using Streamlit and Python, and it features data cleaning, exploration, and predictive modeling to progress through different stages of the game.
Game Overview

You will:

    Clean a messy dataset with missing values.
    Explore the dataset to uncover correlations between variables.
    Use predictive analytics to guess the correct direction the robber is heading.
    You have 2 attempts to make the correct guess at the final stage. Fail, and you’ll need to restart the game!

Requirements

To run this game on your computer, follow the steps below. The game requires Python and several libraries:
Prerequisites

    Python 3.7 or higher: Install Python if you don't have it already. You can download it from python.org.

Dependencies

    Streamlit: To run the web-based interactive UI.
    Pandas: To handle data manipulation.
    NumPy: For numerical operations.
    Matplotlib: For visualizing data.

Installation Guide
Step 1: Clone or Download the Game Repository

You can either download the repository as a zip file from GitHub or clone it using Git.

    Clone the repo:

    git clone https://github.com/yourusername/detective-game.git
    cd detective-game

    Download the zip:
        Go to the repository on GitHub and click on "Code" → "Download ZIP".
        Extract the files to a directory of your choice.

Step 2: Install Dependencies

In your terminal or command prompt, navigate to the directory where you downloaded/cloned the game. Then, use the following command to install all the required libraries:

    pip install -r requirements.txt

This will install the following dependencies:

    streamlit
    pandas
    numpy
    matplotlib

If you're missing any dependencies, you can install them individually using pip install <library>.

Step 3: Run the Game

Once everything is set up, you're ready to run the game!

    Open a terminal or command prompt.
    Navigate to the project folder where the game files are located.
    Run the game using Streamlit by typing the following command:

    streamlit run streamlit_app.py

This will start the game on a local server. Streamlit will open your default web browser, and you should see the game interface running.

Step 4: Playing the Game

Once the game is running:

    Stage 1: Data Cleaning:
        You'll be prompted to clean the dataset by filling in missing values. The game will guide you.
    Stage 2: Data Exploration:
        Explore the dataset and identify the most correlated variable with Crime_Score.
        You will be asked to input your guess to move to the next stage.
    Stage 3: Predictive Modeling:
        You’ll need to predict the robber’s direction using the clues.
        You have 2 attempts to guess the correct direction. If you fail both attempts, you will have to restart the game.

Step 5: Restarting the Game

At any time, you can restart the game:

    After completing or failing any stage, click the "Restart Game" button to start over from the introduction.

Troubleshooting

    If Streamlit is not installed:
        Make sure you run pip install -r requirements.txt to install all dependencies.
    If the game doesn’t launch:
        Make sure your terminal/command prompt is in the correct directory.
        Check if the correct Python version is being used (Python 3.7 or higher).

