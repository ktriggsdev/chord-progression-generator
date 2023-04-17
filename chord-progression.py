import streamlit as st
import numpy as np

# define constants for the frequencies, scales, chords and keys
F = [16.35,17.32,18.35,19.45,20.6,21.83,23.12,24.5,25.96,
     27.5,29.14,30.87]
M = [0, 2, 4, 5, 7, 9, 11]
m = [0, 2, 3, 5, 7, 8, 10]
C = ["maj", "min", "min", "maj", "maj", "min", "dim"]
c = ["min", "dim", "maj", "min", "min", "maj", "maj"]
K = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
S = 22050

def g(k,m,l):
  # generate a random chord progression based on a key (k), mode (m) and length (l)
  s = M if m == "major" else m
  h = C if m == "major" else c
  r = K.index(k)
  d = np.random.randint(1 ,8 ,l)
  p = [K[(r + s[i -1]) %12] + h[i -1] for i in d]
  return p

def s(r,t):
  # synthesize a chord from a root note (r) and a chord type (t)
  i = {"maj": [0 ,4 ,7], 
       "min": [0 ,3 ,7], 
       "dim": [0 ,3 ,6], 
       "aug": [0 ,4 ,8]}
  f = F[K.index(r)]
  n = [f * (2 ** (j /12)) for j in i[t]]
  return n

def p(p):
   # play back a chord progression (p) using st.audio 
   a = np.array([])
   for x in p:
     y = x[:-3]
     z = x[-3:]
     w = s(y,z)
     t = np.linspace(0 ,1 ,S)
     v = np.array([])
     for u in w:
       v += np.sin(2 * np.pi * u * t)
     a = np.append(a,v)
   st.audio(a,S)
