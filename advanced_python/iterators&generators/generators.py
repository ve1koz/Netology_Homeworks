def my_generator(list_):
    new_list = [item for sublist in list_ for item in sublist]
    return new_list


if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]

    for item in my_generator(nested_list):
        print(item)