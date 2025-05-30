# daily_reminder.py

# Step 1: Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Use match-case to handle priorities
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Note: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Step 3: Add time-bound message if applicable
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Step 4: Print final reminder
print("\n" + message)
