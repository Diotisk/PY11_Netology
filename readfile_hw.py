def read_cook_book():
    with open("cook_book.txt") as file:
        cook_book = dict()
        for line in file:
            dish = line.strip()
            # print("Название блюда: {}".format(dish))
            file.readline()
            # print("Число под вопросом: {}".format(some_count))
            ingr_list = []
            for i in file:
                i = i.strip()
                if not i:
                    break
                else:
                    ingredient = dict()
                    # print(line)
                    ingredient_data = i.split("|")
                    ingredient["ingredient_name"] = ingredient_data[0].strip()
                    ingredient["quantity"] = int(ingredient_data[1])
                    ingredient["measure"] = ingredient_data[2].strip()
                    ingr_list.append(ingredient)
            cook_book[dish] = ingr_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book()
    print(cook_book)
    shop_list = {}
    for dish in dishes:
        # print(dish)
        for ingredient in cook_book[dish]:
            # print(ingredient)
            new_shop_list_item = dict(ingredient)
            # print(new_shop_list_item)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
