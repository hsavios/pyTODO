def openFile():
    with open("files/todos.txt", 'r') as file:
        return file.readlines()


def writeFile(todos):
    with open("files/todos.txt", 'w') as file:
        file.writelines(todos)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    match user_action:

        case 'add':
            todo = input("Enter todo: ") + "\n"

            todos = openFile()

            todos.append(todo)

            writeFile(todos)

        case 'show':

            todos = openFile()

            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            todos = openFile()

            print('Existing todos: ', todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            writeFile(todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            todos = openFile()

            index = number - 1

            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            writeFile(todos)

            message = f"Todo {todo_to_remove} was removed from the list."

            print(message)

        case 'exit':
            break

print("Bye!")

