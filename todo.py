# todo.py
tasks = []

def add(task):
    tasks.append(task)

def done(number):
    tasks.pop(number - 1)

def show():
    for i, task in enumerate(tasks, start=1):
        print(f"[{i}] {task}")

def count():
    return len(tasks)

def clear():
    tasks.clear()

if __name__ == "__main__":
    add("Install Git")
    add("Finish the Git lab")
    done(1)
    show()
    print("Tasks left:", count())
