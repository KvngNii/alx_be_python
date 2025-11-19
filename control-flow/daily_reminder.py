# daily_reminder.py
# A program that provides customized reminders for daily tasks

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            print(f"Reminder: {reminder} that requires immediate attention today!")
        else:
            print(f"Reminder: {reminder}. Try to complete it as soon as possible.")
    
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            print(f"Reminder: {reminder} that requires immediate attention today!")
        else:
            print(f"Reminder: {reminder}. Try to complete it when you have time.")
    
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            print(f"Reminder: {reminder} that requires immediate attention today!")
        else:
            print(f"Note: {reminder}. Consider completing it when you have free time.")
    
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
