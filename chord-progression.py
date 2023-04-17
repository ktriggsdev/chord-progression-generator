import streamlit as st
import numpy as np
import io
import wave

SR = 22050
DUR = st.number_input("Please enter a number for the duration")
N = int(SR * DUR)
VOL = 0.5

CHORDS = ["C", "Dm", "Em", "F", "G", "Am", "Bdim"]
FREQS = [[261.63, 329.63, 392.00],
         [293.66, 349.23, 440.00],
         [329.63, 392.00, 493.88],
         [349.23, 440.00, 523.25],
         [392.00, 493.88, 587.33],
         [440.00, 523.25, 659.26],
         [493.88, 587.33, 698.46]]

def generate_chord(freqs):
    chord = np.zeros(N)
    for f in freqs:
        wave = np.sin(2 * np.pi * f * np.arange(N) / SR)
        chord += wave
    chord = VOL * chord / np.max(np.abs(chord))
    return chord

def generate_progression(indices):
    progression = []
    for i in indices:
        chord = generate_chord(FREQS[i])
        progression.append(chord)
    progression = np.concatenate(progression)
    return progression

def sound_to_bytes(sound):
    buffer = io.BytesIO()
    wav = wave.open(buffer, mode="wb")
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(SR)
    wav.writeframes((sound * 32767).astype(np.int16))
    wav.close()
    bytes = buffer.getvalue()
    return bytes

st.title("Chord Progression Generator")
st.subheader("A simple app that generates and plays back random chord progressions")

if st.button("Generate"):
    indices = np.random.randint(0, 7, size=8)
    progression = generate_progression(indices)
    bytes = sound_to_bytes(progression)
    st.text(" ".join([CHORDS[i] for i in indices]))
    st.audio(bytes)
