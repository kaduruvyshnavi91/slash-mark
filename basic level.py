class Task:
    def __init__(self, description, priority='normal'):
        self.description = description
        self.priority = priority
        self.id = id(self)  # Unique ID based on the object's memory address

    def __str__(self):
        return f"[{self.priority}] {self.description} (ID: {self.id})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority='normal'):
        task = Task(description, priority)
        self.tasks.append(task)
        print(f"Task added: {task}")

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"Task removed: {task}")
                return
        print("Task not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(task)

    def prioritize_task(self, task_id, priority):
        for task in self.tasks:
            if task.id == task_id:
                task.priority = priority
                print(f"Task updated: {task}")
                return
        print("Task not found.")

    def recommend_tasks(self, keyword):
        recommendations = [task for task in self.tasks if keyword in task.description]
        if not recommendations:
            print("No recommendations found.")
        else:
            print("Recommended tasks:")
            for task in recommendations:
                print(task)


def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Management App")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Prioritize Task")
        print("5. Recommend Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (normal, high, low): ")
            task_manager.add_task(description, priority)

        elif choice == '2':
            task_id = int(input("Enter task ID to remove: "))
            task_manager.remove_task(task_id)

        elif choice == '3':
            task_manager.list_tasks()

        elif choice == '4':
            task_id = int(input("Enter task ID to prioritize: "))
            priority = input("Enter new priority (normal, high, low): ")
            task_manager.prioritize_task(task_id, priority)

        elif choice == '5':
            keyword = input("Enter keyword for recommendations: ")
            task_manager.recommend_tasks(keyword)

        elif choice == '6':
            print("Exiting the app.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()