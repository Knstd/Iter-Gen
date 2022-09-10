from generator import Flat_generator, Flat_generator_any_depth
from iterator import Flat_iterator, Flat_iterator_any_depth

if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    nested_list2 = [
        ['a', 'b', 'c'],
        ['d', ['e', ['f'], 'h'], False],
        [1, 2, None]
    ]

    print('Задание 1: итератор, который принимает список списков, и возвращает их плоское представление')
    for item in Flat_iterator(nested_list):
        print(item)
    print()

    print('Задание 1: лист комперхеншн')
    flat_list = [item for item in Flat_iterator(nested_list)]
    print(flat_list)
    print()

    print('Задание 2: генератор, который принимает список списков, и возвращает их плоское представление')
    for item in Flat_generator(nested_list):
        print(item)
    print()

    print('Задание 3: итератор, обрабатывающий списки с любым уровнем вложенности')
    for item in Flat_iterator_any_depth(nested_list2):
        print(item)
    print()

    print('Задание 4: генератор, обрабатывающий списки с любым уровнем вложенности')
    for item in Flat_generator_any_depth(nested_list2):
        print(item)
