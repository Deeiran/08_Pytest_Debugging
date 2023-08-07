
class TodoList:
    def __init__(self):
        self.todo_list = []
    
    def add(self, todo):
       self.todo_list.append(todo)        
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos

      
    def incomplete(self):
        return [todo for todo in self.todo_list if not todo.complete]

        #  return [todo for todo in self.todo_list if not todo.complete]
        
        # incomlteList = []
        # for todo in self.todo_list:
        #     if todo.complete == False:
        #         incomlteList.append(todo)
        # return incomlteList
    
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        

    def complete(self):
        return [todo for todo in self.todo_list if todo.complete]
        # return [todo for todo in self.todo_list if todo.complete]
        # completelist = []
        # for todo in self.todo_list:
        #     if todo.complete == True:
        #         completelist.append(todo)
        # return completelist     
        # Returns:
        #   A list of Todo instances representing the todos that are complete
  
    def give_up(self):
        for todo in self.todo_list:
            if not todo.complete:
                todo.mark_complete()

        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
    


