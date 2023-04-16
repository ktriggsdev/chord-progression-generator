import streamlit as st
import librosa

# Define the chord progressions
chords = [
    ["C", "G", "Am", "F"],
    ["Dm", "G", "C", "Am"],
    ["Em", "A", "D", "G"],
    ["Fmaj7", "Bbmaj7", "Ebmaj7", "Abmaj7"],
    ["Bbm7b5", "Ebmaj7", "Abmaj7", "Dbmaj7"],
    ["Gb7b5", "Dbmaj7", "Abmaj7", "Ebmaj7"],
]

# Define the function to generate a chord progression
def generate_chord_progression(key, mode):
    # Get the chords for the given key and mode
    chords_for_key = chords[key]
    chords_for_mode = [chords_for_key[i] for i in mode]

    # Generate a random chord progression
    progression = []
    for i in range(4):
        progression.append(chords_for_mode[np.random.randint(len(chords_for_mode))])

    return progression

# Define the function to play the chord progression
def play_chord_progression(chord_progression):
    # Get the audio files for the chords
    audio_files = [
        librosa.load("chords/{}.wav".format(chord))[0] for chord in chord_progression
    ]

    # Play the audio files
    librosa.output.play(audio_files, sr=44100)

# Create the Streamlit app
st.title("Chord Progression Generator")

# Get the key and mode from the user
key = st.selectbox("Key", ["C", "Dm", "Em", "Fmaj7", "Bbm7b5", "Gb7b5"])
mode = st.selectbox("Mode", ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"])

# Generate a chord progression
chord_progression = generate_chord_progression(key, mode)

# Display the chord progression
st.write("Chord progression: {}".format(chord_progression))

# Play the chord progression
if st.button("Play"):
    play_chord_progression(chord_progression)
