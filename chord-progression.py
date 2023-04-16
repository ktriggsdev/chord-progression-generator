import streamlit as st
import numpy as np
import random

# Define a function to generate a random chord progression
def generate_chord_progression(key, num_chords):
  chords = ["C", "Dm", "Em", "F", "G", "Am", "Bb", "C"]
  progression = []
  for i in range(num_chords):
    progression.append(random.choice(chords))
  return progression

# Create a function to play the chord progression
def play_chord_progression(progression, key):
  # Create a list of frequencies for each chord
  frequencies = []
  for chord in progression:
    frequencies.append(get_frequencies(chord, key))

  # Create a sound object
  sound = np.array(frequencies).astype("float32")

  # Play the sound
  st.audio(sound)

# Define a function to get the frequencies for a chord
def get_frequencies(chord, key):
  # Get the notes in the chord
  notes = get_notes(chord)

  # Get the frequencies for each note
  frequencies = []
  for note in notes:
    frequencies.append(get_frequency(note, key))

  return frequencies

# Define a function to get the notes in a chord
def get_notes(chord):
  # Create a dictionary that maps chords to notes
  chords_to_notes = {
    "C": ["C", "E", "G"],
    "Dm": ["D", "F", "A"],
    "Em": ["E", "G", B],
    "F": ["F", A, C],
    "G": ["G", B, D],
    "Am": ["A", C, E],
    "Bb": ["Bb", D, F],
  }

  # Get the notes for the specified chord
  notes = chords_to_notes[chord]

  return notes

# Define a function to get the frequency of a note
def get_frequency(note, key):
  # Get the frequency of the A note in the specified key
  a_frequency = 440 * 2 ** ((key - 69) / 12)

  # Get the frequency of the specified note
  frequency = a_frequency * 2 ** ((note - 69) / 12)

  return frequency

# Create a title for the app
st.title("Chord Progression Generator")

# Create a text input for the key
key = st.text_input("Key (C, Dm, Em, F, G, Am, Bb)")

# Create a slider for the number of chords
num_chords = st.slider("Number of Chords", 1, 10)

# Generate a random chord progression
progression = generate_chord_progression(key, num_chords)

# Display the chord progression
st.write("Chord Progression:", progression)

# Play the chord progression
play_chord_progression(progression, key)
