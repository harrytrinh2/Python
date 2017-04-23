first_dict = {"one": "mot", "two": "hai", "three": "ba"}
second_dict = {"one": "mot", "two": "hai", "three": "ba", "four": "bon"}
item_first_dict = first_dict.items()
# item_second_dict=second_dict.items()

check = True


def check_contain(first_dict, second_dict):
    print(first_dict, '\n', second_dict)
    first_dict_length = len(first_dict)
    second_dict_length = len(second_dict)
    if first_dict_length > second_dict_length:
        check = False
    else:
        for key, value in item_first_dict:
            if key not in second_dict[key]:
                check = False
                break
    return check

check_contain(first_dict, second_dict)
print(check)
# if __name__ == '__main__':
#     if check_contain(first_dict, second_dict):
#         print(check)
#     else:
#         print(check)
