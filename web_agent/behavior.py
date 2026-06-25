import random
import time
import numpy as np

def human_delay(target_seconds=2.0, deviation=0.5):
    """
    Simulates human reading/reaction time using a Gaussian distribution.
    Instead of exactly 2.0s, a human might take 1.84s or 2.31s.
    """
    # Generates a random number around the target average
    delay = np.random.normal(target_seconds, deviation)
    # Ensure the delay never drops below a realistic human minimum limit (e.g., 0.2 seconds)
    delay = max(0.2, delay) 
    
    print(f"[Brain] Simulating human cognitive pause: {delay:.2f} seconds.")
    time.sleep(delay)

def human_coordinates(x, y, variance=4):
    """
    Humans never click the exact same pixel twice. 
    Adds a slight random offset to simulate imperfect human finger taps/mouse clicks.
    """
    offset_x = x + random.randint(-variance, variance)
    offset_y = y + random.randint(-variance, variance)
    print(f"[Brain] Target calculated at ({x}, {y}) -> Humanized to ({offset_x}, {offset_y})")
    return offset_x, offset_y
