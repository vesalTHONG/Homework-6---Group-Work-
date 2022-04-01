from typing import Iterable
def remove_all_after(items: list, border: int) -> Iterable:
    try:
        return items[:items.index(border) + 1]
    except ValueError:
        return items
if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_after([1, 2, 3, 4, 5], 3)))
    assert list(remove_all_after([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
    assert list(remove_all_after([1, 1, 2, 2, 3, 3], 2)) == [1, 1, 2]
    print("Coding complete?")
