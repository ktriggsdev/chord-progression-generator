import streamlit as st
import numpy as np
import random

# Define the chord progressions
chords = [
    [0, 4, 7],
    [2, 6, 9],
    [4, 7, 11],
    [5, 9, 12],
    [7, 11, 14],
]

# Define the function to generate a random chord progression
def generate_chord_progression():
    return random.choice(chords)

# Create the Streamlit app
st.title("Chord Progression Generator")

# Create a slider to control the number of chords in the progression
num_chords = st.slider("Number of chords", 1, 5)

# Generate a random chord progression
chord_progression = generate_chord_progression()

# Create a table to display the chord progression
st.table(chord_progression)

# Create a button to play the chord progression
play_button = st.button("Play")

# If the play button is clicked, play the chord progression
if play_button:
    # Create a list of notes for the chord progression
    notes = []
    for chord in chord_progression:
        notes.append(np.array([chord[0], chord[1], chord[2]]))

    # Play the notes
    streamlit.audio(notes, format="wav")
