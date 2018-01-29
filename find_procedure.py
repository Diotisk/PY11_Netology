import os


migrations = "Migrations"
current_dir = os.path.dirname(os.path.abspath(__file__))
print("Current working directory: ", current_dir)

new_current_dir = os.path.abspath(migrations)
print("New current working directory: ", new_current_dir)
print("All files in the new cwd: ", os.listdir(new_current_dir))


def search_files_cwd(extension, cwd):
    searched_files = []
    for file in os.listdir(cwd):
        i = os.path.splitext(file)
        if extension == i[1]:
            searched_files.append(file)
    print("SQL files only: ", searched_files)
    print("Number of SQL files: ", len(searched_files))
    return searched_files


def search_files(files_list):
    count = 0
    searched_item = input("Search for: ")
    new_list = []
    for file in files_list:
        print(file, len(files_list))
        with open(file, "r") as content:
            content_list = content.read()
            print(content_list)
            if searched_item in content_list:
                new_list.append(file)
                count += 1
    for k in new_list:
        print(k)
    print(count)
    search_files(new_list)


if __name__ == '__main__':
    sql_files = search_files_cwd(".sql", new_current_dir)
    search_files(sql_files)
    pass
