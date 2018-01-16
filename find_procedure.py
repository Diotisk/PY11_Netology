import os


migrations = "Migrations"
current_dir = os.path.dirname(os.path.abspath(__file__))
print("Current working directory: ", current_dir)

os.chdir(migrations)
new_current_dir = os.getcwd()
print("New current working directory: ", new_current_dir)
# print("All files in the new cwd: ", os.listdir(new_current_dir))


def search_files_cwd(extension, cwd):
    searched_files = []
    for file in os.listdir(cwd):
        i = os.path.splitext(file)
        if extension in i:
            searched_files.append(file)
    # print("SQL files only: ", searched_files)
    # print("Number of SQL files: ", len(searched_files))
    return searched_files

sql_files = search_files_cwd(".sql", new_current_dir)


def search_files(files_list):
    count = 0
    f = input("Search for: ")
    new_list = []
    for j in files_list:
        with open(j, "r") as content:
            content_list = content.read()
            if f in content_list:
                # print(j)
                new_list.append(j)
                count += 1
    for k in new_list: print(k)
    print(count)
    search_files(new_list)


search_files(sql_files)


# if __name__ == '__main__':
#
#     pass
