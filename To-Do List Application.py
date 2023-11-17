class Task:
    def _init_(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False
class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for idx, task in enumerate(self.tasks):
            print(f"{idx + 1}. Description: {task.description}")
            print(f"   Due Date: {task.due_date}")
            print(f"   Priority: {task.priority}")
            print(f"   Status: {'Completed' if task.completed else 'Not Completed'}")
            print("-" * 30)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def update_task(self, task_index, new_description, new_due_date, new_priority):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].description = new_description
            self.tasks[task_index].due_date = new_due_date
            self.tasks[task_index].priority = new_priority
            print("Task updated successfully.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task.description}' removed successfully.")
        else:
            print("Invalid task index.")

# Sample usage of the ToDoList class
todo_list = ToDoList()

while True:
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Mark Task as Completed")
    print("4. Update Task")
    print("5. Remove Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter task description: ")
        due_date = input("Enter due date: ")
        priority = input("Enter priority: ")
        new_task = Task(description, due_date, priority)
        todo_list.add_task(new_task)

    elif choice == "2":
        todo_list.display_tasks()

    elif choice == "3":
        task_index = int(input("Enter task index to mark as completed: ")) - 1
        todo_list.mark_task_as_completed(task_index)

    elif choice == "4":
        task_index = int(input("Enter task index to update: ")) - 1
        new_description = input("Enter new task description: ")
        new_due_date = input("Enter new due date: ")
        new_priority = input("Enter new priority: ")
        todo_list.update_task(task_index, new_description, new_due_date, new_priority)

    elif choice == "5":
        task_index = int(input("Enter task index to remove: ")) - 1
        todo_list.remove_task(task_index)

    elif choice == "6":
        print("Exiting To-Do List Application. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")