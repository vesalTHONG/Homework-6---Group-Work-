from typing import Iterable
def remove_all_after(items: list, border: int) -> Iterable:
    try:
        return items[:items.index(border) + 1]
    except ValueError:
        return items
