file_name = 'file.txt'

def new_file():
    f = open(file_name, "w")
    print("The new file has been created")


def num_of_lines():
    f1 = open(file_name, "r")
    a = f1.readlines()
    print("The number of lines present in the file are : ", len(a))


def num_of_chars():
    f2 = open(file_name, "r")
    f2.read()
    noc = f2.tell()
    print("The total characters present in the file are: ", noc - 1)


def append_at_end():
    content = input("Enter the content you want to add at the end: ")
    f3 = open(file_name, "a")
    f3.write(content)
    f3.close()


def replace_a_line():
    replace_line = int(input("Enter the line you want to replace: "))
    content = input("Enter the content you want to replace: ")

    fl = open(file_name, "r")
    lns = fl.readlines()
    fl.close()
    flo = open(file_name, "w")
    lns[replace_line - 1] = content + "\n"
    flo.writelines(lns)
    flo.close()


def insert_a_line():
    line = int(input("In which line you want to insert: "))
    con = input("What content do you want to insert: ")

    file = open(file_name, 'r')
    lns = file.readlines()
    file.close()
    fl = open(file_name, "w")
    lns.insert(line, con + "\n")
    fl.writelines(lns)
    fl.close()


while True:
    opt = int(input("Enter the option you want: "))

    if opt == 1:
        new_file()
    elif opt == 2:
        num_of_chars()
    elif opt == 3:
        num_of_chars()
    elif opt == 4:
        append_at_end()
    elif opt == 5:
        replace_a_line()
    elif opt == 6:
        insert_a_line()
    elif opt ==7:
        print("Exiting Program..........")
        break
    else:
        print("Wrong option!!")
