from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import random
import time

def safe_input_simulator():
    # Initialize controllers
    keyboard = KeyboardController()
    mouse = MouseController()

    # Numbers to choose from
    choices = ['1', '2', '3', '4', '5']
    size = 0

    while(size < 1 or size > 5):
        # Determines how long the choice array will be
        size = int(input("How many abilites do you have: "))
        if(size < 1 or size > 5):
            print("Please enter a valid number")

    choices = choices[:size]

    try:
        print("Starting input simulation in 5 seconds...")
        print("Press Ctrl+C to stop")
        time.sleep(5)  # Give user time to switch windows if needed
        last = 0
        
        while True:
            # Randomly select and press a number
            number = random.choice(choices)

            if(size != 1):
                # Makes sure that the new number is not the last number
                while(last == number):
                    number = random.choice(choices)

                keyboard.press(number)
                keyboard.release(number)
                
                # Perform mouse click
                mouse.press(Button.left)
                mouse.release(Button.left)

                trick = {1:0.25, 2:0.5, 3:0.75, 4:1.0, 5:1.25, 6:1.3}
                
                # Add a small delay between actions
                time.sleep(float(1 + trick[int(number)]))
            
                last = number
            else:
                keyboard.press(number)
                keyboard.release(number)
                
                # Perform mouse click
                mouse.press(Button.left)
                mouse.release(Button.left)
                
                time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nSimulation stopped by user")

if __name__ == "__main__":
    # Add safety prompt
    print("This script will simulate keyboard and mouse inputs.")
    print("Please ensure you're running this in an appropriate application.")
    
    safe_input_simulator()