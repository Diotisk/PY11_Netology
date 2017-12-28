cook_book = dict()
ingredient_dict = dict()
ingredient_list = []

def search_ingredient():
    for line in file:
        if len(line) > 1:
            #print(line)
            f = line.split("|")
            ingredient_dict["ingredient_name"] = f[0]
            ingredient_dict["quantity"] = int(f[1])
            ingredient_dict["measure"] = f[2].strip()
            print(ingredient_dict)
        else:
            break
    return ingredient_dict

with open("cook_book.txt") as file:
    for line in file:
        dish = file.readline()
        print(dish.strip())
        person_count = int(file.readline())
        print(person_count)
        search_ingredient()