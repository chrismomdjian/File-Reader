def main():
    user_file = input("Please enter a filename or type 'quit' to exit: ")
    #user_file = user_file.lower()
    if user_file == "quit":
        return

    file_exists = True

    try:
        open_file = open(user_file, "r")
    except FileNotFoundError:
        file_exists = False
        while file_exists == False:
            print("That file was not found")
            user_file = input("Please enter a filename or type 'quit' to exit: ")
            user_file = user_file.lower()
            if user_file == "quit":
                return

            try:
                open_file = open(user_file, "r")
                file_exists = True
            except FileNotFoundError:
                file_exists = False

    counter = 0
    lines = open_file.readline()

    print("---Beginning of document---\n")

    while lines != "":
        counter += 1
        lines = lines.strip("\n")
        print(str(counter) + ". " + lines)
        lines = open_file.readline()

    open_file.close()

    print("\n---This is the end of the document---")
    
main()
