from lib.todo import *

"""
when we contract with a task
we get the task reflected in the todo of the proprty
"""
def contract_with_task():
    todo = Todo("go to the park")
    assert todo.task == "go to the park"

"""
when we contract the task as incomplete
then task is initially incomplete
"""
def test_task_is_incomplete():
    todo = Todo("go to the park")   
    assert todo.complete == False


"""
when we contract with a task
then task is initially complete
"""
def test_task_is_complete():
    todo = Todo("go to the park")  
    todo.mark_complete()
    assert todo.complete == True
