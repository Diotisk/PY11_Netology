from pprint import pprint

with open("cook_book.txt") as file:

    def read_cook_book():
        dishes = []
        cook_book = dict()

        for line in file:
            dish = line.strip()
            # print("Название блюда: {}".format(dish))
            dishes.append(dish)
            person_count = int(file.readline())
            # print("Количество гостей: {}".format(person_count))
            ingridient_list = []
            for line in file:
                if len(line) > 1:
                    ingridient = dict()
                    # print(line)
                    f = line.split("|")
                    ingridient["ingridient_name"] = f[0]
                    ingridient["quantity"] = int(f[1])
                    ingridient["measure"] = f[2].strip()
                    ingridient_list.append(ingridient.copy())
                else:
                    break
            cook_book[dish] = ingridient_list
        return cook_book


    #
    # def read_cook_book():
    #     global dishes
    #     dishes = []
    #     for line in file:
    #         dish = line.strip()
    #         # print("Название блюда: {}".format(dish))
    #         dishes.append(dish)
    #         global person_count
    #         person_count = int(file.readline())
    #         # print("Количество гостей: {}".format(person_count))
    #
    #         def form_ingridient_list():
    #             global ingridient_list
    #             ingridient_list = []
    #             for line in file:
    #                 line = line.strip()
    #                 if not line:
    #                     break
    #                 else:
    #                     ingridient = dict()
    #                     # print(line)
    #                     f = line.split("|")
    #                     ingridient["ingridient_name"] = f[0].strip()
    #                     ingridient["quantity"] = int(f[1])
    #                     ingridient["measure"] = f[2].strip()
    #                     ingridient_list.append(ingridient.copy())
    #             return ingridient_list
    #
    #         form_ingridient_list()
    #         global cook_book
    #         cook_book = dict()
    #         cook_book[dish] = ingridient_list
    #         #pprint(cook_book)
    #         return cook_book
    #
    # pprint(read_cook_book())


    read_cook_book()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        # print(dish)
        for ingridient in cook_book[dish]:
            # print(ingridient)
            new_shop_list_item = dict(ingridient)

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
    person_count  # = int(input('Введите количество человек: '))
    dishes  # = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()