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