import tkinter as tk
import pygame

# Initialize pygame
pygame.mixer.init()

# Function to play a specific musical note
def play_note(music_note):
    pygame.mixer.Sound(music_note).play()

# Main window for the GUI
window = tk.Tk()
window.title("Piano")

# Mapping of keys to their corresponding sound files
keys = {
    "C": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/C.wav",
    "D": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/D.wav",
    "E": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/E.wav",
    "F": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/F.wav",
    "G": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/G.wav",
    "A": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/A.wav",
    "B": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/B.wav",
    "C1": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/C1.wav",
    "D1": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/D1.wav",
    "E1": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/E1.wav",
    "F1": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/F1.wav",
    "C#": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/C_s.wav",
    "D#": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/D_s.wav",
    "F#": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/F_s.wav",
    "G#": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/G_s.wav",
    "Bb": "/Users/miasooklal/Desktop/CompSciPrincipals/Music_Notes/Bb.wav"
}

# Create buttons for each white key
white_keys = ["C", "D", "E", "F", "G", "A", "B", "C1", "D1", "E1", "F1"]
for i, key in enumerate(white_keys):
    btn = tk.Button(window, text=key, bd=12, width=9, height=18, font=('arial', 16, 'bold'))
    btn.grid(row=1, column=i, sticky="nsew")
    btn.config(command=lambda k=key: play_note(keys[k]))

# Create buttons for each black key
black_keys = ["C#", "D#", "F#", "G#", "Bb"]
for i, key in enumerate(black_keys):
    btn = tk.Button(window, text=key, bd=12, width=5, height=12, font=('arial', 16, 'bold'), bg='black', fg='black')
    if key == "Bb":  # Special case for positioning the last black key
        btn.grid(row=0, column=2 * i + 1, sticky="nsew", padx=(0, 2))
        btn.config(command=lambda k=key: play_note(keys[k]))
    else:
        btn.grid(row=0, column=2 * i + 1, sticky="nsew", padx=(0, 2))
        btn.config(command=lambda k=key: play_note(keys[k]))

# Configure grid sizes
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(list(range(len(white_keys))), weight=1)

# Start the GUI event loop
window.mainloop()
