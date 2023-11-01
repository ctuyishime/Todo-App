FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    """ Read a text file and return the list of
    to-do items."""
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print(__name__)
if __name__ == '__main__':
    print(get_todos())
