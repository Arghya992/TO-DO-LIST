#  To-Do List App (Python + TXT)

A simple command-line **To-Do List application** built using Python.\
All tasks are stored permanently using a **CSV file (tasks.txt)**.

It includes:

-   ✔ Add new tasks\
-   ✔ View pending tasks\
-   ✔ Mark tasks as completed\
-   ✔ Delete tasks\
-   ✔ Auto file creation + txt storage

------------------------------------------------------------------------

##  Project Structure

    project-folder/
    │── todo.py
    │── tasks.txt   (auto-created on first run)
    │── README.md

------------------------------------------------------------------------

##  How to Run

1.  Install Python (3.13.9 recommended)
2.  Save all project files in one folder
3.  Run the script:

``` bash
python todo.py
```

The application will automatically create **tasks.txt** on the first
run.

------------------------------------------------------------------------

##  TXT Format

The application stores tasks in this format:

    task,status
    Buy groceries,pending
    Finish project,done

-   **task** → task description\
-   **status** → `pending` or `done`

------------------------------------------------------------------------

##  Features Explained

### 1️ Add Task

Adds a new task to the txt with status set to `pending`.

### 2️ View Pending Tasks

Displays all tasks that are still incomplete.

### 3️ Mark Task Completed

Select a task and update its status to `done`.

### 4️ Delete Task

Shows all tasks and allows deleting any by number.

### 5️ Auto-Saving

Every action updates `tasks.txt` instantly.

------------------------------------------------------------------------

##  Source Code

The complete code is available in **todo.py**.

------------------------------------------------------------------------

##  Possible Enhancements

You can extend this project with:

-   GUI (Tkinter)
-   JSON or SQLite storage
-   Class-based OOP version
-   Colorful CLI interface
-   Task deadlines or priority system
-   Sorting & filtering features

<h3>Arghyadeep Gope</h3>
<h3>25BAI10710</h3>
<h3>Vityarthi Project</h3>