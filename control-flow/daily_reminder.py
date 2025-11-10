task = input ("please enter your task: ")
priority = input ("Priority (high, medium, low): ")
time_bound = input ("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        priority_level = "high Priority task"
    case "medium":
        priority_level = "medium Priority task"
    case "low":
        priority_level = "low Priority task"
    case _:
        priority_level = "unknown priority task"

match time_bound:
    case "yes":
        time_level = "that requires immediate attention today!"
    case "no":
        time_level = ". Consider completing it when you have free time."
    case _:
        time_level = "an unspecified time-bound status"

if time_bound == "yes":
    print (f"Reminder: '{task}' is a {priority_level}  {time_level} ")
if time_bound == "no":
    print (f"Note: '{task}' is a {priority_level} {time_level} ")