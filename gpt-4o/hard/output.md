Here’s a simple To-Do List Web App using HTML, CSS, and JavaScript with clear comments and explanations. It includes:
	•	Adding new tasks
	•	Marking tasks as complete/incomplete
	•	Removing tasks
	•	Clean and responsive styling

⸻

✅ How It Works (Beginner Explanation):
	1.	HTML sets up the structure (title, input box, task list).
	2.	CSS styles the app (layout, colors, spacing).
	3.	JavaScript handles the behavior (adding, toggling, deleting tasks).

⸻

🧾 Full Code (all in one file for simplicity):

You can copy and paste this into a .html file and open it in your browser.

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Simple To-Do List</title>
  <style>
    /* Basic reset and layout */
    * {
      box-sizing: border-box;
      font-family: Arial, sans-serif;
    }

    body {
      background: #f4f4f4;
      padding: 20px;
      display: flex;
      justify-content: center;
    }

    .todo-container {
      background: white;
      padding: 20px;
      border-radius: 10px;
      width: 100%;
      max-width: 400px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    h1 {
      text-align: center;
      color: #333;
    }

    #new-task {
      width: 100%;
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 5px;
      margin-bottom: 10px;
    }

    #add-task {
      width: 100%;
      padding: 10px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      margin-bottom: 20px;
    }

    #add-task:hover {
      background-color: #0056b3;
    }

    ul {
      list-style-type: none;
      padding: 0;
    }

    li {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #f9f9f9;
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 5px;
      margin-bottom: 10px;
    }

    li.completed span {
      text-decoration: line-through;
      color: #888;
    }

    .actions {
      display: flex;
      gap: 8px;
    }

    .actions button {
      background: none;
      border: none;
      cursor: pointer;
      font-size: 14px;
      padding: 5px;
    }

    .complete-btn {
      color: green;
    }

    .delete-btn {
      color: red;
    }
  </style>
</head>
<body>
  <div class="todo-container">
    <h1>My To-Do List</h1>
    <input type="text" id="new-task" placeholder="Add a new task...">
    <button id="add-task">Add Task</button>
    <ul id="task-list"></ul>
  </div>

  <script>
    // Get references to DOM elements
    const newTaskInput = document.getElementById("new-task");
    const addTaskButton = document.getElementById("add-task");
    const taskList = document.getElementById("task-list");

    // Function to add a new task
    function addTask() {
      const taskText = newTaskInput.value.trim(); // Remove extra spaces

      if (taskText === "") {
        alert("Please enter a task.");
        return;
      }

      // Create a new list item <li>
      const li = document.createElement("li");

      // Create a span to hold the task text
      const span = document.createElement("span");
      span.textContent = taskText;

      // Create action buttons (complete and delete)
      const actions = document.createElement("div");
      actions.classList.add("actions");

      const completeBtn = document.createElement("button");
      completeBtn.textContent = "✓";
      completeBtn.classList.add("complete-btn");

      const deleteBtn = document.createElement("button");
      deleteBtn.textContent = "🗑";
      deleteBtn.classList.add("delete-btn");

      // Add buttons to the actions div
      actions.appendChild(completeBtn);
      actions.appendChild(deleteBtn);

      // Add span and actions to the list item
      li.appendChild(span);
      li.appendChild(actions);

      // Add the list item to the task list
      taskList.appendChild(li);

      // Clear the input
      newTaskInput.value = "";

      // Event: Mark task as complete/incomplete
      completeBtn.addEventListener("click", () => {
        li.classList.toggle("completed");
      });

      // Event: Delete the task
      deleteBtn.addEventListener("click", () => {
        li.remove();
      });
    }

    // When the "Add Task" button is clicked
    addTaskButton.addEventListener("click", addTask);

    // When Enter key is pressed in the input field
    newTaskInput.addEventListener("keypress", function (e) {
      if (e.key === "Enter") {
        addTask();
      }
    });
  </script>
</body>
</html>


⸻

🧠 Summary:
	•	HTML sets up the layout: input field, button, task list.
	•	CSS makes it visually clean with padding, borders, and colors.
	•	JavaScript adds dynamic behavior:
	•	Add task: Creates a new list item.
	•	Complete task: Toggles line-through style.
	•	Delete task: Removes the item from the list.

Let me know if you’d like a version that saves the list in local storage so it persists after refreshing the page!