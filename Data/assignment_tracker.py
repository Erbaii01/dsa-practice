
assignments = [
    {
        "course": "MFCS",
        "title": "Problem Set 4",
        "due": "2026-10-15",
        "completed": False
    },
    {
        "course": "Probability",
        "title": "Problem Set 5",
        "due": "2026-10-18",
        "completed": True
    },
    {
        "course": "Python",
        "title": "Assignment 2",
        "due": "2026-10-20",
        "completed": False
    }
]
count=0
for assignment in assignments:
    if assignment['completed']==False:
        count+=1
print(f"You have {count} unfinished assignments.")
        
