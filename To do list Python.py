class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: {task}")

    def update_task(self, task_number, updated_task):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["task"] = updated_task
            print(f"Updated task {task_number + 1}: {updated_task}")
        else:
            print("Invalid task number")

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            print(f"Completed task {task_number + 1}")
        else:
            print("Invalid task number")

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            deleted_task = self.tasks.pop(task_number)
            print(f"Deleted task: {deleted_task['task']}")
        else:
            print("Invalid task number")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i + 1}. {task['task']} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Display Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_number = int(input("Enter the task number to update: ")) - 1
            updated_task = input("Enter the updated task: ")
            todo_list.update_task(task_number, updated_task)
        elif choice == '3':
            task_number = int(input("Enter the task number to complete: ")) - 1
            todo_list.complete_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_number)
        elif choice == '5':
            todo_list.display_tasks()
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()