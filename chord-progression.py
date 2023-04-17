import streamlit as st
import numpy as np
import io
import wave

st.title("Chord Progression Generator")
st.subheader("A simple app that generates and plays back random chord progressions")

SR = 22050
DUR = st.number_input("Please enter a number for the duration")
N = int(SR * DUR)
VOL = 0.5

CHORDS = ["C", "Cm", "C7", "D", "Dm", "D7", "E", "Em", "E7", "F", "Fm", "F7", "G", "Gm", "G7", "A", "Am", "A7", "B", "Bm", "B7"]
FREQS = [[261.63, 329.63, 392.00], # C major
         [261.63, 311.13, 392.00], # C minor
         [261.63, 329.63, 392.00, 466.16], # C dominant seventh
         [293.66, 369.99, 440.00], # D major
         [293.66, 349.23, 440.00], # D minor
         [293.66, 369.99, 440.00, 523.25], # D dominant seventh
         [329.63, 415.30, 493.88], # E major
         [329.63, 392.00, 493.88], # E minor
         [329.63, 415.30, 493.88, 587.33], # E dominant seventh
         [349.23, 440.00, 523.25], # F major
         [349.23, 415.30, 523.25], # F minor
         [349.23, 440.00, 523.25, 622.25], # F dominant seventh
         [392.00, 493.88, 587.33], # G major
         [392.00, 466.16, 587.33], # G minor
         [392.00, 493.88, 587.33, 698.46], # G dominant seventh
         [440.00, 554.37, 659.26], # A major
         [440.00, 523.25, 659.26], # A minor
         [440.00, 554.37, 659.26, 783.99], # A dominant seventh
         [493.88, 622.25, 739.99], # B major
         [493.88, 587.33, 739.99], # B minor
         [493.88, 622.25, 739.99, 880] ] # B dominant seventh


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



if st.button("Generate"):
    indices = np.random.randint(0, 7, size=8)
    progression = generate_progression(indices)
    bytes = sound_to_bytes(progression)
    st.text(" ".join([CHORDS[i] for i in indices]))
    st.audio(bytes)
