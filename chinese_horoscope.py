
import tkinter as tk
from tkinter import messagebox

# Chinese Zodiac signs and years
zodiac_signs = {
    0: 'Monkey',
    1: 'Rooster',
    2: 'Dog',
    3: 'Pig',
    4: 'Rat',
    5: 'Ox',
    6: 'Tiger',
    7: 'Rabbit',
    8: 'Dragon',
    9: 'Snake',
    10: 'Horse',
    11: 'Goat'
}

# Compatibility data (sample)
compatibility = {
    'Monkey': ['Rat', 'Dragon', 'Rooster'],
    'Rooster': ['Ox', 'Snake', 'Monkey'],
    'Dog': ['Tiger', 'Rabbit', 'Horse'],
    'Pig': ['Goat', 'Rabbit', 'Tiger'],
    'Rat': ['Dragon', 'Monkey', 'Ox'],
    'Ox': ['Snake', 'Rooster', 'Rat'],
    'Tiger': ['Dog', 'Horse', 'Pig'],
    'Rabbit': ['Goat', 'Pig', 'Dog'],
    'Dragon': ['Monkey', 'Rat', 'Rooster'],
    'Snake': ['Rooster', 'Ox', 'Dragon'],
    'Horse': ['Tiger', 'Dog', 'Goat'],
    'Goat': ['Rabbit', 'Pig', 'Horse']
}

def get_zodiac(year):
    # Chinese Zodiac repeats every 12 years
    return zodiac_signs[year % 12]

def show_zodiac():
    try:
        year = int(entry.get())
        if year < 0:
            raise ValueError("Year cannot be negative.")
        zodiac = get_zodiac(year)
        compatibility_signs = ', '.join(compatibility[zodiac])
        messagebox.showinfo("Zodiac Result", f"Your Chinese Zodiac sign is: {zodiac}.
Compatible with: {compatibility_signs}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid year (numbers only).")

# Tkinter GUI setup
root = tk.Tk()
root.title("Chinese Horoscope Calculator")

# Instructions
label = tk.Label(root, text="Enter your birth year to calculate your Chinese Zodiac sign:")
label.pack(pady=10)

# Entry for user to input year
entry = tk.Entry(root)
entry.pack(pady=5)

# Button to trigger the zodiac calculation
button = tk.Button(root, text="Find My Zodiac", command=show_zodiac)
button.pack(pady=10)

# Run the application
root.mainloop()
