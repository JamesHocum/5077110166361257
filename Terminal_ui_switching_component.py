# UI Switching Component (Part of Terminal Application)

def switch_theme(theme_name):
    global current_theme
    if theme_name in UI_THEMES:
        current_theme = theme_name
        apply_theme()  # Re-apply the theme
    else:
        print("Invalid theme name.")

# Example usage within the main loop:
# (Assuming the 'handle_input' function is part of the terminal app)
def handle_input():
    while True:
        apply_theme()
        command = input(f"[{get_os_type()}] >>> ")
        if command.lower() == 'exit':
            break
        elif command.lower().startswith('theme '):
            theme_name = command.split(' ')[1]
            switch_theme(theme_name) # Call the switch_theme function
        elif command.lower() == 'clear':
            clear_screen()
        else:
            run_command(command)