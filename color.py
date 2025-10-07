import time
import os
from colorama import init, Fore, Style
import random

# Initialize colorama for colored terminal output
init()

# List of colors to cycle through
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

# ASCII art for the spinner
spinner = [
    "   |   ",
    "  /    ",
    " /     ",
    "/      ",
    "      \\ ",
    "     \\  ",
    "    \\   ",
    "   |   ",
]

# Fun message to display
message = "Code for Fun!"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_frame(frame, color):
    clear_screen()
    # Center the spinner and message
    print("\n" * 5)  # Add some vertical padding
    for line in spinner:
        print(" " * 20 + color + line + Style.RESET_ALL)  # Center horizontally
    print("\n" + " " * (20 - len(message)//2) + color + message + Style.RESET_ALL)
    time.sleep(0.1)

# Main animation loop
try:
    while True:
        for i in range(len(spinner)):
            # Choose a random color for each frame
            color = random.choice(colors)
            display_frame(i, color)

except KeyboardInterrupt:
    # Graceful exit on Ctrl+C
    clear_screen()
    print(" " * 20 + Fore.CYAN + "Thanks for playing!" + Style.RESET_ALL)