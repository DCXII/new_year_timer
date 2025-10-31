import time
import os
import random
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii(lines):
    for line in lines:
        print(line)
    print()

def show_fortune():
    fortunes = [
        "A new chapter begins — make it legendary.",
        "This year will bring you unexpected joy.",
        "Fortune favors your courage this year.",
        "Dream big. The universe is listening.",
        "This year, your hard work will pay off."
    ]
    print(f"\nFortune: {random.choice(fortunes)}")

current_year = datetime.now().year
next_year = current_year + 1

print(f"Counting down to {next_year}...")
time.sleep(2)

# Countdown loop
while True:
    now = datetime.now()
    new_year = datetime(next_year, 1, 1, 0, 0, 0)
    remaining = new_year - now

    if remaining.total_seconds() <= 0:
        break

    # Calculate days, hours, minutes, seconds
    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    clear_screen()
    print(f"COUNTDOWN TO {next_year}\n")
    print(f"Time left: {days:02}d {hours:02}h {minutes:02}m {seconds:02}s")
    time.sleep(1)

# Clear screen and print celebration
clear_screen()

# Print HAPPY
print_ascii([
    "██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗   ██╗",
    "██║  ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝",
    "███████║███████║██████╔╝██████╔╝ ╚████╔╝ ",
    "██╔══██║██╔══██║██╔═══╝ ██╔═══╝   ╚██╔╝  ",
    "██║  ██║██║  ██║██║     ██║        ██║   ",
    "╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝   "
])

time.sleep(1)

# Print NEW
print_ascii([
    "███╗   ██╗███████╗██╗    ██╗",
    "████╗  ██║██╔════╝██║    ██║",
    "██╔██╗ ██║█████╗  ██║ █╗ ██║",
    "██║╚██╗██║██╔══╝  ██║███╗██║",
    "██║ ╚████║███████╗╚███╔███╔╝",
    "╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝ "
])

time.sleep(1)

# Print YEAR
print_ascii([
    "██╗   ██╗███████╗ █████╗ ██████╗ ",
    "╚██╗ ██╔╝██╔════╝██╔══██╗██╔══██╗",
    " ╚████╔╝ █████╗  ███████║██████╔╝",
    "  ╚██╔╝  ██╔══╝  ██╔══██║██╔══██╗",
    "   ██║   ███████╗██║  ██║██║  ██║",
    "   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝"
])

print(f"\nHAPPY NEW YEAR {next_year}!")
show_fortune()

