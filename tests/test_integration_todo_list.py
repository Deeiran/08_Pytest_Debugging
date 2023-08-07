from lib.todo import *
from lib.todo_list import *

"""
when I add multible todo task 
and return the list of the task
in the incomplete list. 
"""
def test_add_two_task_and_list_them():
    todolist = TodoList()
    task_1 = Todo("go to the park")
    task_2 = Todo("play with friends")
    todolist.add(task_1)
    todolist.add(task_2)
    assert todolist.incomplete() == [task_1, task_2]
"""
when I add multible todo task 
and makd one as complete
it doesn't show up in the incomplete list
"""
def test_add_two_task_and_add_complted_first_task():
    todolist = TodoList()
    task_1 = Todo("go to the park")
    task_2 = Todo("play with friends")
    todolist.add(task_1)
    todolist.add(task_2)
    task_1.mark_complete()
    assert todolist.incomplete() == [task_2]

# """
# add two todo task and marked task_1 under complted 
# and return the completed task list.
# """
def test_add_two_task_and_add_complted_first_task_show_completed():
    todolist = TodoList()
    task_1 = Todo("go to the park")
    task_2 = Todo("play with friends")
    todolist.add(task_1)
    todolist.add(task_2)
    task_1.mark_complete()
    assert todolist.complete() == [task_1]

# """
# add two todo task and marked task_1 under complted 
# and giveup the todo list 
# by marking other incompleted list as completed
# """
def test_to_give_up_all_list():
    todolist = TodoList()
    task_1 = Todo("go to the park")
    task_2 = Todo("play with friends")
    todolist.add(task_1)
    todolist.add(task_2)
    task_1.mark_complete()
    assert todolist.give_up() == None