import json

FILE_NAME = "assignments.json"
# Load assignments from JSON
def load_assignments():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            print("Invalid assignment data!")
            return []
        return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Invalid JSON file!")
        return []

# Save assignments to JSON
def save_assignments(assignments):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(assignments, f, indent=4)
    print("Assignments saved!")


# Show unfinished assignments
def show_pending(assignments):
    found = False
    for assignment in assignments:
        if not assignment["completed"]:
            print(assignment["title"])
            found = True
    if not found:
        print("No pending assignments!")


# Add a new assignment
def add_assignment(assignments, title):
    title = title.strip()
    if not title:
        print("Assignment title cannot be empty!")
        return
    for assignment in assignments:
        if assignment["title"].lower() == title.lower():
            print("Assignment already exists!")
            return

    assignments.append({
        "title": title,
        "completed": False
    })

    print("Assignment added!")

# Mark an assignment as completed
def complete_assignment(assignments, title):
    for assignment in assignments:
        if assignment["title"].lower() == title.strip().lower():
            assignment["completed"] = True
            print("Assignment completed!")
            return
    print("Assignment not found!")

# Main program
def main():
    assignments=load_assignments()
    while True:
        print("\n===== Assignment Manager =====")
        print("1. Show pending assignments")
        print("2. Add assignment")
        print("3. Complete assignment")
        print("4. Save and exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_pending(assignments)
        elif choice == "2":
            title = input("Enter assignment title: ")
            add_assignment(assignments, title)
        elif choice == "3":
            title = input("Enter assignment to complete: ")
            complete_assignment(assignments, title)
        elif choice == "4":
            save_assignments(assignments)
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
