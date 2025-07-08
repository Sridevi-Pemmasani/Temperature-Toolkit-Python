from temperature_toolkit.generalutils import *

# List to store temperature records
records = []

def main_menu():
    while True:
        print("\n*********************************************************************************************************\nChoose an operation:")
        for key, desc in operations.items():
            print(f"{key}. {desc}")
        choice = input("Enter your choice: ").strip()
        if choice in operations:
            handle_menu_choice(choice,records)
        else:
            print("Invalid choice. Try again.")

# Menu options mapped to functions
operations = {
    '1': ("Create New Temperature Record"),
    '2': ("View All Temperature Records"),
    '3': ("Modify Existing Temperature Record"),
    '4': ("Delete Existing Temperature Record"),
    '5': ("Convert Temperatures of Selected Day"),
    '6': ("Show Temeratures Summary - All Days"),
    '7': ("Are Temperatures Above a Given Threshold - Selected Day?"),
    '8': ("Average Temperature - All Days"),
    '9': ("Show Hottest Day"),
    '10': ("Show Extreme Days Recorded Temperature Above a Threshold"),
    '11': ("Show Temperature Ranges - All Days"),
    '12': ("Show Temperature Trend"),
    '13': ("Detect Spike"),   
    '14': ("Exit")
}

if __name__ == "__main__":
    main_menu()
