from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Calculate and display a future date based on user input.
    Prompts the user for the number of days to add to the current date.
    """
    # Get the number of days from the user
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Get current date
    current_date = datetime.now()
    
    # Calculate the future date
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    """
    Main function to run the datetime exploration script.
    """
    # Part 1: Display the current date and time
    display_current_datetime()
    
    # Part 2: Calculate a future date
    calculate_future_date()

if __name__ == "__main__":
    main()
