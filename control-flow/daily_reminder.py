# daily_reminder.py

# Prompt for task inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the message prefix
reminder_msg = f"Reminder: '{task}' is a {priority} priority task"

# Use match-case to handle different priorities
match priority:
    case "high" | "medium" | "low":
        if time_bound == "yes":
            reminder_msg += " that requires immediate attention today!"
        else:
            reminder_msg += ". Consider completing it when you have free time."
    case _:
        reminder_msg = f"Reminder: '{task}' has an unknown priority level. Please check the input."

# Print the final reminder
print(reminder_msg)
