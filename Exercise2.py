def index_power(array, N):
    return array[N] ** N if len(array) > N else -1

if __name__ == '__main__':
    print("example:")
    print(index_power([102, 98, 77, 45, 109], 3))

    assert index_power([1, 2, 3, 4], 2) == 9, "sqaure"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Coding complete")
