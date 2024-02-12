class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.counter_items_id = 0
        self.counter_list_id = 0
        return self

    def __next__(self):
        if len(self.list_of_list) == self.counter_list_id:
            raise StopIteration
        current_list = self.list_of_list[self.counter_list_id]
        current_item = current_list[self.counter_items_id]
        self.counter_items_id +=1
        if len(current_list) == self.counter_items_id:
            self.counter_items_id = 0
            self.counter_list_id += 1
        return current_item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
