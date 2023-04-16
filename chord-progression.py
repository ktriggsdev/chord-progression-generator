import streamlit as st
import numpy as np
import pyaudio
import wave

# Define the chord progressions
chord_progressions = [
    ["C", "G", "Am", "F"],
    ["Dm", "G", "Am", "C"],
    ["Em", "A", "Dm", "G"],
    ["F", "C", "G", "Am"],
]

# Define the function to generate a chord progression
def generate_chord_progression(key, mode):
    chords = []
    for chord in chord_progressions:
        chords.append(get_chord(key, mode, chord))
    return chords

# Define the function to get a chord
def get_chord(key, mode, chord):
    if mode == "major":
        notes = [
            key + 0,
            key + 4,
            key + 7,
            key + 9,
            key + 12,
        ]
    elif mode == "minor":
        notes = [
            key + 0,
            key + 3,
            key + 7,
            key + 9,
            key + 12,
        ]
    return notes

# Define the function to play a chord progression
def play_chord_progression(chords):
    # Create a PyAudio object
    audio = pyaudio.PyAudio()

    # Open a stream
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
        frames_per_buffer=1024,
        output=True,
    )

    # Play the chord progression
    for chord in chords:
        # Generate the notes
        notes = np.array(chord)

        # Convert the notes to frequencies
        frequencies = 2**(notes / 12) * 440

        # Generate a sine wave for each frequency
        waves = np.sin(2 * np.pi * frequencies * np.arange(1024) / 44100)

        # Combine the waves into a single audio signal
        audio_signal = np.sum(waves, axis=0)

        # Write the audio signal to the stream
        stream.write(audio_signal.astype(np.int16))

    # Close the stream
    stream.close()

    # Close the PyAudio object
    audio.terminate()

# Create a Streamlit app
app = st.beta_app()

# Add a title
st.title("Chord Progression Generator")

# Add a key selector
key = st.selectbox("Key", ["C", "Dm", "Em", "F", "G", "Am"])

# Add a mode selector
mode = st.selectbox("Mode", ["major", "minor"])

# Generate a chord progression
chords = generate_chord_progression(key, mode)

# Play the chord progression
if st.button("Play"):
    play_chord_progression(chords)

# Display the chord progression
st.write("Chord progression:", chords)
