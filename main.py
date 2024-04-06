import os

prompt_file = False
csv_file = False

def clear_console():
    # Clear the console based on the OS
    if os.name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')
    else:
        # Unsupported OS
        print("Clearing the console is not supported on this operating system.")


def check_files():
    if os.path.exists("prompt.txt"):
        print(">Prompt Template Found.")
    else:
        print(">Prompt Template Missing")
    
    if os.path.exists("key-values.csv"):
        print(">CSV File Found.")
    else:
        print(">CSV File Missing")


def ask_choice(title: str, options: list):
    while True:
        print(title+":")
        for index , item in iter(options):
            print(f"{index}. {item}")
            
        selection = input()
        if type(selection) is not int:
            print
        if selection > 0 and selection <= len(options):
            return selection - 1
        
        
    






clear_console()
print('Welcome to Python Prompt Generator.\n')
print('Please wait. Checking for required files and perimeters...')
check_files()
ask_choice("Select mode", ["Normal Mode" , "Description Mode (won't include title in  prompt.)"])