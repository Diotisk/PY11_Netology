def read_cook_book():
    with open("cook_book.txt") as file:
        cook_book = dict()
        for line in file:
            dish = line.strip()
            # print("Название блюда: {}".format(dish))
            file.readline()
            # print("Число под вопросом: {}".format(some_count))

            def form_ingridient_list():
                ingr_list = []
                for i in file:
                    i = i.strip()
                    if not i:
                        break
                    else:
                        ingridient = dict()
                        # print(line)
                        f = i.split("|")
                        ingridient["ingridient_name"] = f[0].strip()
                        ingridient["quantity"] = int(f[1])
                        ingridient["measure"] = f[2].strip()
                        ingr_list.append(ingridient.copy())
                return ingr_list

            ingridient_list = form_ingridient_list()
            cook_book[dish] = ingridient_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book()
    shop_list = {}
    for dish in dishes:
        # print(dish)
        for ingridient in cook_book[dish]:
            # print(ingridient)
            new_shop_list_item = dict(ingridient)
            # print(new_shop_list_item)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
