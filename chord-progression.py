import streamlit as st
import numpy as np
import random

# Define the chord progressions
chord_progressions = [
    ["C", "G", "Am", "F"],
    ["Dm", "G", "C", "Am"],
    ["Em", "A", "D", "G"],
    ["F", "C", "G", "Am"],
]

# Define the function to generate a random chord progression
def generate_chord_progression():
    # Get a random chord progression from the list
    progression = random.choice(chord_progressions)

    # Convert the chord progression to a list of notes
    notes = []
    for chord in progression:
        notes.extend(np.array(chord))

    # Return the list of notes
    return notes

# Create the Streamlit app
st.title("Chord Progression Generator")

# Get the user input
key = st.selectbox("Key", ["C", "Dm", "Em", "F"])
scale = st.selectbox("Scale", ["Major", "Minor"])

# Generate a random chord progression
progression = generate_chord_progression()

# Play the chord progression
st.audio(progression, format="wav")

# Display the chord progression
st.write("Chord progression:", progression)
