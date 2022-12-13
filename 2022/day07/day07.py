def format_text(txt):
    text = []
    for line in txt.splitlines():
        text.append(line)
    return text

# Return a list of all the directories in the filesystem
def get_directories(txt):
    directories = {}
    for command in txt:
        # Check if line is referencing a directory (also ignore 'cd ..' commands)
        if ("cd " in command) and ("cd .." not in command):
            # Add the directory name to the directories array
            dir_name = command[(command.index('cd ') + 3):]
            if dir_name not in directories: # Make sure there are no duplicates
                directories.update({(command[(command.index('cd ') + 3):]): []})
    return directories


# Calculate size of the directory
def calc_dir_size(dir): # Parameter is the directory name

    # Find the items that appear under '$ ls'
    index = 0
    for command in commands:
        if command == "$ ls":
            # Get the name of the current diretory selected
            current_directory = commands[(index - 1)][(commands[(index - 1)].index('cd ') + 3):]
            # print(f"LS command for the '{current_directory}' directory")

            # find all the items that appear in the directory
            total_size = 0
            cursor_index = index
            cursor = commands[cursor_index + 1]
            while ("$ " not in cursor):
                cursor = commands[cursor_index + 1]
                # If the file is a simple file -> add the file size to the total size
                if ("dir " not in cursor) and ("$ " not in cursor):
                    print(cursor[:cursor.index(" ")])
                    total_size += int(cursor[:cursor.index(" ")])
                # If the file is a directory -> add the size of the directory to the total size

                cursor_index += 1
            print(f"Total size of {current_directory}: {total_size}")

            
            # If folder has another folder within in -> we need to get the size of that folder

            # add the directory name and the size to a dictionary {name: size}
        index += 1
    size = 0

    return size

# Need to find the instance of a directory
# Then find when the $ ls command is called for that directory
# If there is a dir within the dir then check if that dir already has an assigned size
    # If it does, then add that size to the total
    # If it DOESNT, then do the same process again for the directory (recursion)
# And basically do that for each directory in directories

# LETS START AGAIN

def calculate_size(directory, contents):
    
    print(f"Calcuating size of '{directory}'")
    print(f"It's contents: {contents}")

    return

def main(commands):
    # Start with an empty path
    path = []
    for command in commands:
        # Check if command is changing directory
        if 'cd ' in command:
            # Check if going backwards a level
            if ' ..' in command:
                # Remove last item in path to go back to previous level
                path.pop()
            else:
                path.append(command[(command.index('cd ') + 3):])
            print(f"PATH: {path}")
        elif '$ ls' in command:
            # function to fetch all the items in that directory
            print(f"Listing items in '{path[-1]}'")
            items = []
            # Find where the listed items end
            comm = f"$ cd {path[-1]}"

            for n in commands[((commands.index(comm)) + 2):]:
                if '$' in n:
                    calculate_size(path[-1], items)
                    print(f"Looking past: {commands[((commands.index(comm)) + 2)]}")
                    break
                else:
                    # Add items under the 'ls' command into an array
                    print(f"adding {n} to list of items")
                    items.append(n)
            
    return





if __name__ == '__main__':
    with open('test.txt') as inputs:
        f = inputs.read()
    commands = format_text(f)

    # print(commands)

    directories = get_directories(commands)
    # print(f"Directories: {directories}")




    print(main(commands))


# Script is bad

