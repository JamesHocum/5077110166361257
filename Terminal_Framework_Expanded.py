# UI Framework - Terminal Application (Expanded)
import os
import platform
import subprocess
import sys
import threading
import time
import json # For saving and loading settings

# --- UI Configuration ---
UI_THEMES = {
    "modern": {
        "bg_color": "#2e3440",
        "text_color": "#d8dee9",
        "prompt_color": "#8fbcbb",
        "cursor_color": "#81a1c1",
        "font": "Consolas",
    },
    "retro_80s": {
        "bg_color": "#000000",
        "text_color": "#00ff00",  # Green
        "prompt_color": "#00ffff",  # Cyan
        "cursor_color": "#00ff00",
        "font": "Courier New",
    },
    "90s_matrix": {
        "bg_color": "#000000",
        "text_color": "#00ff00", # Green
        "prompt_color": "#00ff00",
        "cursor_color": "#00ff00",
        "font": "Courier New",
    },
     "2000s_vista": {
        "bg_color": "#0066cc", # Blue
        "text_color": "#ffffff", # White
        "prompt_color": "#ffff00", # Yellow
        "cursor_color": "#ffffff",
        "font": "Arial",
    },
    # Add more themes as desired, matching decades or styles
}

current_theme = "modern"  # Default theme

# --- Helper Functions ---
def get_os_type():
    os_name = platform.system()
    if os_name == 'Windows':
        return 'Windows'
    elif os_name == 'Darwin':
        return 'macOS'
    elif os_name == 'Linux':
        return 'Linux'
    else:
        return 'Unknown'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print(f"Error: {result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
    except FileNotFoundError:
        print(f"Command not found.")

# --- Theme Application (OS-Specific) ---
def apply_theme():
    theme = UI_THEMES[current_theme]
    os_type = get_os_type()

    if os_type == 'Windows':
        # Windows-specific color and font setting (using ANSI escape codes)
        os.system(f'color 07') # default colors
        os.system(f'mode con cols=80 lines=25')  # Set console size (adjust as needed)
        # Note: Windows font setting via command line is complex and may require external tools
        # Consider using a library like 'colorama' for cross-platform color support
    elif os_type == 'macOS' or os_type == 'Linux':
        # macOS/Linux specific color and font setting (ANSI escape codes)
        # Colors using ANSI escape codes
        print(f"\033[48;2;{int(theme['bg_color'][1:3], 16)};{int(theme['bg_color'][3:5], 16)};{int(theme['bg_color'][5:7], 16)}m", end="") # Background
        print(f"\033[38;2;{int(theme['text_color'][1:3], 16)};{int(theme['text_color'][3:5], 16)};{int(theme['text_color'][5:7], 16)}m", end="") # Text
        print(f"\033[38;2;{int(theme['prompt_color'][1:3], 16)};{int(theme['prompt_color'][3:5], 16)};{int(theme['prompt_color'][5:7], 16)}m", end="") # Prompt
        # Font setting (using terminal specific commands or config)
        # This part is generally more complex and depends on the terminal emulator
        # You may need to use external tools or configure the terminal directly
    else:
        print("Unsupported OS for theme application.")
    print(f"Theme applied: {current_theme}") # Debug

# --- Persistent Settings (Saving and Loading) ---
SETTINGS_FILE = "terminal_settings.json"

def load_settings():
    global current_theme
    try:
        with open(SETTINGS_FILE, 'r') as f:
            settings = json.load(f)
            current_theme = settings.get('theme', current_theme) # Load theme
    except FileNotFoundError:
        pass # Use default settings
    except json.JSONDecodeError:
        print("Error loading settings. Using defaults.")
        pass

def save_settings():
    settings = {'theme': current_theme}
    try:
        with open(SETTINGS_FILE, 'w') as f:
            json.dump(settings, f)
    except Exception as e:
        print(f"Error saving settings: {e}")

# --- Main Interaction Loop ---
def handle_input():
    while True:
        apply_theme() # Apply the theme
        command = input(f"[{get_os_type()}] >>> ")
        if command.lower() == 'exit':
            save_settings() # Save settings on exit
            break
        elif command.lower().startswith('theme '):
            theme_name = command.split(' ')[1]
            if theme_name in UI_THEMES:
                global current_theme
                current_theme = theme_name
                apply_theme() # Apply the new theme
            else:
                print("Invalid theme.")
        elif command.lower() == 'clear':
            clear_screen()
        else:
            run_command(command)

# --- Main Execution ---
def main():
    load_settings() # Load settings at start
    clear_screen()
    apply_theme()
    print("Welcome to the Terminal Application!")
    handle_input()
    print("Exiting Terminal.")

if __name__ == "__main__":
    main()