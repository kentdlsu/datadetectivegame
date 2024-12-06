import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# ---------- Data Preparation ----------
# Generate a synthetic dataset
def generate_dataset():
    np.random.seed(42)
    data = {
        "Robber_ID": ["Robber1"] * 100,
        "Age": np.random.randint(20, 50, size=100),
        "Height_cm": np.random.normal(170, 10, size=100),
        "Weight_kg": np.random.normal(70, 15, size=100),
        "Crime_Score": np.random.randint(50, 100, size=100),
        "Direction_Clue": ["North", "East", "South", "West"] * 25,
    }
    df = pd.DataFrame(data)
    # Add missing values
    df.loc[df.sample(frac=0.2).index, 'Height_cm'] = np.nan
    df.loc[df.sample(frac=0.2).index, 'Weight_kg'] = np.nan
    return df

# Save the dataset
dataset = generate_dataset()

# ---------- Game Logic ----------
# Introduction
def introduction():
    st.title("Crack the Pattern to Catch the Robber!")
    st.markdown("""
    You are a detective solving a string of mysterious robberies.  
    Use data cleaning, exploration, and predictive analytics to track the robber's next move.
    """)
    st.button("Begin Investigation", on_click=lambda: st.session_state.update(stage="data_cleaning"))

# Data Cleaning Stage
def data_cleaning():
    st.header("Stage 1: Data Cleaning")
    st.write("The dataset has some missing values. Your task is to clean it! Make sure to download the CSV file and run it in Jupyter Notebook!")
    
    st.write(dataset.head())
    
    user_code = st.text_area("What's the code to be used in order to clean up the missing values? Enter it below!", height=200)
    if st.button("Run Code"):
        try:
            exec(user_code, globals())
            if not dataset.isnull().values.any():
                st.success("Great! You've cleaned the data. Proceed to the next stage.")
                st.button("Next Stage", on_click=lambda: st.session_state.update(stage="data_exploration"))
            else:
                st.error("There are still missing values in the dataset. Try again.")
        except Exception as e:
            st.error(f"Error in your code: {e}")

# Data Exploration Stage
def data_exploration():
    st.header("Stage 2: Data Exploration")
    st.write("Explore the dataset to find clues.")
    
    st.markdown("Use `Crime_Score` and other variables to uncover patterns.")
    question = st.text_input("Which variable highly correlates with Crime_Score?")
    correct_answer = "Age"
    
    if question:
        if question.lower() == correct_answer.lower():
            st.success("Correct! You found the key clue. Let's move on.")
            st.button("Next Stage", on_click=lambda: st.session_state.update(stage="predictive_modeling"))
        else:
            st.error("Incorrect. Try again!")

# Predictive Modeling Stage
def predictive_modeling():
    st.header("Stage 3: Predictive Modeling")
    st.write("Build a predictive model to determine the robber's direction.")
    
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0

    st.markdown("""
    Use linear regression to predict the `Crime_Score` based on variables like Age, Height, or Weight.  
    Based on the model, infer the robber's likely direction. Use the given clues and data patterns to predict the robber's direction.  
    You have **2 attempts** to get it right!
    """)
    
    correct_direction = "North"

    # Example model building
    X = dataset[["Age"]]
    y = dataset["Crime_Score"]
    model = LinearRegression().fit(X, y)
    predictions = model.predict(X)
    r2 = r2_score(y, predictions)
    
    st.write(f"Model R² score: {r2:.2f}")
    
    direction_guess = st.text_input("Which direction is the robber heading (North, East, South, West)?")
    if st.button("Submit Answer"):
        if not direction_guess:
            st.error("Please enter a direction before submitting.")
        elif direction_guess.lower() == correct_direction.lower():
            st.success("Congratulations! You caught the robber!")
            st.button("Restart Game", on_click=lambda: st.session_state.update(stage="introduction", attempts=0))
        else:
            st.session_state.attempts += 1
            if st.session_state.attempts < 2:
                st.error(f"Incorrect! You have {2 - st.session_state.attempts} attempts left.")
            else:
                st.error("You've used all your attempts. Game over! Please restart.")
                st.button("Restart Game", on_click=lambda: st.session_state.update(stage="introduction", attempts=0))
# ---------- Main App Logic ----------
def main():
    st.sidebar.title("Detective Game")
    if "stage" not in st.session_state:
        st.session_state["stage"] = "introduction"
    
    if st.session_state["stage"] == "introduction":
        introduction()
    elif st.session_state["stage"] == "data_cleaning":
        data_cleaning()
    elif st.session_state["stage"] == "data_exploration":
        data_exploration()
    elif st.session_state["stage"] == "predictive_modeling":
        predictive_modeling()

if __name__ == "__main__":
    main()
