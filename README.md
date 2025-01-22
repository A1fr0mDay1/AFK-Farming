# Input Simulation Script

A Python script that simulates keyboard number presses and mouse clicks with customizable delays. This tool allows you to automate repetitive inputs to stay online while afk in games.

## Prerequisites

Before running this script, you'll need to install the required Python package:

```bash
pip install pynput
```

## Features

- Simulates keyboard number presses (1-5)
- Automatically clicks the mouse after each number press to use selected ability
- Prevents the same number from being pressed twice in a row
- Customizable number of abilities (1-5)
- Variable delays between actions based on the number pressed
- Safe exit using Ctrl+C
- Input validation to ensure proper number selection

## How It Works

1. The script prompts you to specify how many abilities you have (1-5)
2. It creates a list of numbers based on your input
3. After a 5-second delay, it begins:
   - Randomly selecting a number from your list
   - Pressing that number key
   - Clicking the mouse
   - Waiting for a variable delay before the next action

## Delay Times

The delay after each number press is calculated as: 1 second + additional time based on the number pressed:
- Number 1: +0.25 seconds
- Number 2: +0.50 seconds
- Number 3: +0.75 seconds
- Number 4: +1.00 seconds
- Number 5: +1.25 seconds

## Usage

1. Run the script:
```bash
python input_simulator.py
```

2. Confirm you want to proceed when prompted

3. Enter the number of abilities (1-5)

4. Switch to your target application within the 5-second countdown

5. The script will run until you press Ctrl+C

## Safety Features

- Confirmation prompt before starting
- 5-second delay before input simulation begins
- Input validation for number of abilities
- Easy exit using Ctrl+C
- Prevention of duplicate consecutive inputs

## Important Notes

- Ensure you're running this script in the appropriate application
- Make sure you have the necessary permissions for input simulation
- Test in a safe environment first
- Be ready to use Ctrl+C to stop the script if needed

## Requirements

- Python 3.x
- pynput library

## Warning

This script simulates keyboard and mouse inputs. Use it responsibly and ensure you're using it in an appropriate context where automated inputs are allowed.
