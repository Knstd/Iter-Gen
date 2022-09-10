def Flat_generator(my_list):
    for item in my_list:
        if isinstance(item, list):
            for nested_list in item:
                yield nested_list
        else:
            yield item


def Flat_generator2(my_list):
    return (item for nested_list in my_list for item in nested_list)


def Flat_generator_any_depth(my_list):
    for item in my_list:
        if isinstance(item, list):
            for nested_list in Flat_generator_any_depth(item):
                yield nested_list
        else:
            yield item
