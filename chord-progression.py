import streamlit as st
import numpy as np
import random

# Define the chord progressions
chord_progressions = [
    ["C", "G", "Am", "F"],
    ["Dm", "G", "C", "Am"],
    ["E", "A", "D", "G"],
    ["F#m", "B", "E", "A"],
]

# Define the function to generate a random chord progression
def generate_chord_progression():
    # Choose a random chord progression
    progression = random.choice(chord_progressions)

    # Return the chord progression
    return progression

# Define the function to play the chord progression
def play_chord_progression(progression):
    # Create a list of notes
    notes = []
    for chord in progression:
        notes.extend(chord)

    # Create a synthesizer
    synthesizer = st.audio.synth()

    # Play the notes
    synthesizer.play(notes)

# Create the app
st.title("Chord Progression Generator")

# Generate a random chord progression
progression = generate_chord_progression()

# Display the chord progression
st.write("Chord progression:", progression)

# Play the chord progression
play_chord_progression(progression)
