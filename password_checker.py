class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority  # 1 (High), 2 (Medium), 3 (Low)

    def __str__(self):
        priority_labels = {1: "P1", 2: "P2", 3: "P3"}
        return f"{self.name} [Priority: {priority_labels.get(self.priority, 'Unknown')}]"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority):
        task = Task(name, priority)
        self.tasks.append(task)
        print(f"Added: {task}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\n📋 Task List (Sorted by Priority):")
        for i, task in enumerate(sorted(self.tasks, key=lambda x: x.priority)):
            print(f"{i + 1}. {task}")

    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print(f"Removed task: {task}")
                return
        print("Task not found.")


def menu():
    manager = TaskManager()
    while True:
        print("\n--- Task Manager Menu ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            name = input("Enter task name: ")
            try:
                priority = int(input("Enter priority (1=High, 2=Medium, 3=Low): "))
                if priority not in [1, 2, 3]:
                    raise ValueError
                manager.add_task(name, priority)
            except ValueError:
                print("Invalid priority. Please enter 1, 2, or 3.")
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            name = input("Enter task name to remove: ")
            manager.remove_task(name)
        elif choice == '4':
            print("Exiting Task Manager. Bye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
