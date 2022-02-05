from json import dump
from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:

        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)
            with open('dict.json', 'w', encoding='utf-8') as f:
                all_list = zip_longest((' '.join(us.split(',')) for us in users), hobby, fillvalue=None)
                my_dict = {str(element[0]).strip(): str(element[1]).strip() for element in all_list}

                dump(my_dict, f, ensure_ascii=False)
            print(my_dict)
        else:
            exit(1)