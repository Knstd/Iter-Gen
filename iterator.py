from itertools import chain


class Flat_iterator:

    def __init__(self, lst):
        self.lst = lst
        self.list_index = 0
        self.nested_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.list_index < len(self.lst):
            if not isinstance(self.lst[self.list_index], list):
                self.list_index += 1
                return self.lst[self.list_index - 1]
            else:
                if self.nested_index != len(self.lst[self.list_index]):
                    self.result = self.lst[self.list_index][self.nested_index]
                    self.nested_index += 1
                    return self.result
                else:
                    self.list_index += 1
                    self.nested_index = 0
        raise StopIteration


class Flat_iterator2:  # с использованием itertools

    def __init__(self, my_list):
        self.my_list = my_list

    def __iter__(self):
        return chain.from_iterable(self.my_list)


class Flat_iterator_any_depth:

    def __init__(self, my_list):
        self.my_list = my_list
        self.list_index = 0

    def __iter__(self):
        self.item = iter(self.my_list)
        return self

    def __next__(self):
        next_item = next(self.item)
        if not isinstance(next_item, list):
            self.list_index += 1
            return next_item
        else:
            self.item = chain(next_item, self.item)
            return next(self.item)
