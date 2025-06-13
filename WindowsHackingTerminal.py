pyinstaller

import os
import sys
import subprocess
import platform
import shutil

# --- Configuration ---
APP_NAME = "Violet Terminal"
VERSION = "1.0"
AUTHOR = "Lady Violet"
DESCRIPTION = "A powerful, customizable terminal application."
ICON_FILE = "violet_icon.ico"  # Replace with your icon file
BRANDING_IMAGE = "violet_branding.png"  # Replace with your branding image (optional)
# --- UI Theme Variables (Example - Adjust as needed) ---
BACKGROUND_COLOR = "#000000"  # Black
TEXT_COLOR = "#00ff00"  # Green
FONT_FAMILY = "Consolas"
FONT_SIZE = 12

# --- Function Definitions ---

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    """Displays the application header with branding."""
    clear_screen()
    print(f" {APP_NAME} - Version {VERSION} ")
    print(f" {DESCRIPTION} ")
    print(f" (C) {AUTHOR} ")
    print("-" * 40)  # Separator

def run_command(command):
    """Executes a shell command and returns the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return None, f"Error: {e}\n{e.stderr}"
    except FileNotFoundError:
        return None, "Error: Command not found."

def get_platform_info():
    """Get OS and architecture info"""
    return platform.platform(), platform.machine()


def main_loop():
    """Main application loop."""
    display_header()
    platform_info, arch_info = get_platform_info()
    print(f"Running on: {platform_info} ({arch_info})")
    print("\nType 'help' for commands or 'exit' to quit.")

    while True:
        try:
            command = input(f"\n{APP_NAME} > ")
            command = command.strip()

            if command.lower() == "exit":
                break
            elif command.lower() == "help":
                display_help()
            elif command.lower() == "clear":
                clear_screen()
                display_header()
            elif command.lower() == "about":
                display_header() # Redundant, but can add more app-specific info here
            elif command.lower() == "platform":
                platform_info, arch_info = get_platform_info()
                print(f"Operating System: {platform_info}")
                print(f"Architecture: {arch_info}")
            else:
                output, error = run_command(command)
                if output:
                    print(output.strip())
                if error:
                    print(error.strip())
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def display_help():
    """Displays a help message."""
    print("\nAvailable Commands:")
    print("  help      - Displays this help message.")
    print("  clear     - Clears the terminal screen.")
    print("  about     - Displays application information.")
    print("  platform  - Displays platform information.")
    print("  exit      - Exits the application.")
    print("  [command] - Executes a shell command (e.g., 'dir', 'ls', 'ping').")
    print("\nNote:  Be cautious when executing commands. Incorrect commands can have unintended consequences.")


# --- Branding and Customization (Example) ---

def apply_branding():
    """Applies custom branding (e.g., loading an image)."""
    # In a real application, this would handle loading an image and displaying it.
    # For this example, we'll just print a message.
    if os.path.exists(BRANDING_IMAGE):
        print(f"\n*Loading Branding Image: {BRANDING_IMAGE}...*")
        # You would use an image library (like PIL/Pillow) to display the image.
    else:
        print("\n*No branding image found.*")

# --- Main Execution ---

if __name__ == "__main__":
    # apply_branding()  # Uncomment to enable branding (if you have a branding image)
    main_loop()
