task = input("Enter your task: ")
priority = input("(high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")



match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a {priority} priority task that requires immediate action today!")
        else:
            print(f"{task} is a {priority} priority task that does not require immediate action today!")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a {priority} priority task that requires immediate action today!")
        else:
            print(f"{task} is a {priority} priority task that does not require immediate action today!")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a {priority} priority task that requires immediate action today!")
        else:
            print(f"{task} is a {priority} priority task that does not require immediate action today!")
