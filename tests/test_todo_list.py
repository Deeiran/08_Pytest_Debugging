from lib.todo_list import *

"""
initially, the incompleted task list is empty
"""
def test_initially_has_an_empty_todo_list():
    todolist = TodoList()
    assert todolist.todo_list == []

"""
initially, the completed task list is empty
"""
def test_initially_has_an_empty_complete_list():
    todolist = TodoList()
    assert todolist.todo_list == []

"""
initially, the give up list is empty
"""
def test_initially_has_an_empty_give_up_list():
    todolist = TodoList()
    assert todolist.todo_list == []

