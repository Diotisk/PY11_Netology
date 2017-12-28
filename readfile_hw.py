cook_book = dict()
ingredient_dict = dict()
ingredient_list = [ingredient_dict]

def search_ingredient():
    for line in file:
        if len(line) > 1:
            f = line.split("|")
            #print(f)
            ingredient_dict["ingredient_name"] = f[0]
            ingredient_dict["quantity"] = f[1]
            ingredient_dict["measure"] = f[2].strip()
            #print(ingredient_dict)
        else:
            break
        ingredient_list.append(ingredient_dict)
        #print(ingredient_list)
    return ingredient_dict

with open("cook_book.txt") as file:
    for line in file:
        dish = line
        #print(dish.strip())
        person_count = int(file.readline())
        #print(person_count)
        search_ingredient()
        cook_book[dish] = ingredient_list
    print(cook_book)