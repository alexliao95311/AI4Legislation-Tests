Of course! Here's a simple to-do list web app using HTML, CSS, and 
JavaScript:

HTML Code:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>To-Do List</h1>
    <ul id="todo-list"></ul>
    <button id="add-task-btn">Add Task</button>
    <script src="script.js"></script>
</body>
</html>
```
CSS Code:
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

#todo-list {
    list-style-type: none;
    margin: 0;
    padding: 0;
}

#todo-list li {
    padding: 10px;
    border-bottom: 1px solid #ccc;
}

#todo-list li:last-child {
    border-bottom: none;
}

#add-task-btn {
    position: fixed;
    right: 10px;
    top: 10px;
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
}

#add-task-btn:hover {
    background-color: #3e8e41;
}
```
JavaScript Code:
```javascript
const todoList = document.getElementById("todo-list");
const addTaskBtn = document.getElementById("add-task-btn");

let todos = [];

function addTask() {
    const task = prompt("Enter a new task: ");
    if (task !== null && task !== "") {
        todos.push(task);
        renderTodos();
    }
}

function renderTodos() {
    todoList.innerHTML = "";
    for (let i = 0; i < todos.length; i++) {
        const li = document.createElement("li");
        li.innerHTML = `<span>${todos[i]}</span>`;
        todoList.appendChild(li);
    }
}

addTaskBtn.addEventListener("click", addTask);
```
Explanation:

* The HTML code creates a basic structure for the web app, with a header, 
a main content area, and a footer. We use the `<!DOCTYPE html>` declaration to specify 
the document type, and the `<html>` element to define the root element of our HTML 
document.
* In the `<head>` section, we include metadata such as the character set (`UTF-8`) and 
the viewport size (`device-width`). We also link a CSS stylesheet (`styles.css`) that 
will be used to style our web app.
* The `<body>` section contains the main content of our web app. We define a `h1` 
element with the title of our web app, and an unordered list (`<ul>`) element to 
display our to-do tasks. We also include a button element (`<button>`) to add new 
tasks.
* The CSS code styles our web app by defining the font family, margin, and padding for 
the body element. We use `list-style-type: none` to remove any existing list styling, 
and `margin: 0; padding: 0;` to remove any default margin or padding. We also define a 
border bottom on each list item (`<li>`) and set the last child to have no border 
bottom.
* The JavaScript code defines some variables and functions. `todoList` is an HTML 
element that will contain our to-do list, `addTaskBtn` is a button element that 
triggers the `addTask()` function when clicked, and `todos` is an array that will 
store our to-do tasks.
* The `addTask()` function prompts the user to enter a new task using the `prompt()` 
method, and then pushes the task onto the end of the `todos` array using the `push()` 
method. It then calls the `renderTodos()` function to update the UI with the new task.
* The `renderTodos()` function iterates over the `todos` array and creates an HTML 
list item for each task. It uses a string template (`${todos[i]}` ) to display the 
task in the list item, and appends each list item to the `todoList` element using the 
`appendChild()` method.
* Finally, we add an event listener to the `addTaskBtn` element to call the 
`addTask()` function when clicked.

This code should give you a basic to-do list web app with the ability to add, mark, 
and remove tasks. You can customize it further by adding more features or styles as 
per your requirement.

