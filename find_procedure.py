import os


migrations = "Migrations"
current_dir = os.path.dirname(os.path.abspath(__file__))
# print("Current working directory: ", current_dir)

new_current_dir = os.path.abspath(migrations)
# print("New current working directory: ", new_current_dir)
# print("All files in the new cwd: ", os.listdir(new_current_dir))


def search_files_cwd(extension, cwd):
    searched_files = []
    for file in os.listdir(cwd):
        i = os.path.splitext(file)
        if extension == i[1]:
            searched_files.append(file)
    # print("SQL files only: ", searched_files)
    # print("Number of SQL files: ", len(searched_files))
    return searched_files


def search_files(files_list):
    searched_item = input("Введите строку: ")
    new_list = []
    for file in files_list:
        with open(os.path.join(new_current_dir, file), "r") as content:
            content = content.read()
            if searched_item in content:
                    new_list.append(file)
    print("Всего: ", len(new_list))
    search_files(new_list)


if __name__ == '__main__':
    sql_files = search_files_cwd(".sql", new_current_dir)
    search_files(sql_files)
    pass
