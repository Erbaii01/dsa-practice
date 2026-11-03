from assignment_manager import count_pending
from assignment_manager import add_assignment
def test_count_pending():
    assignments=[
        {"title": "Assignment 1", "completed": False},
        {"title": "Assignment 2", "completed": True},
        {"title": "Assignment 3", "completed": False}
    ]
    assert count_pending(assignments) == 2
def test_add_assignment():
    assignments=[]
    add_assignment(assignments, "Learn SQL")
    assert len(assignments)==1
    assert assignments[0]["title"]=="Learn SQL"
    assert assignments[0]["completed"]==False

    