def field(items: tuple[dict] | list[dict], *args: str):

    if type(items) not in (list, tuple):
        raise TypeError("Wrong goods format! Try correct types.")

    if not (len(args) > 0):
        raise RuntimeError('No keys specified to print!')

    if tuple(arg for arg in args if arg in items[0].keys()) != args:
        raise KeyError('Selected keys are not in goods list!')

    if len(args) == 1:
        for product in items:
            yield product[args[0]]
    else:
        for product in items:
            yield {arg: product[arg] for arg in args}


if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]

    print("Testing...")

    # Testing
    assert tuple(i for i in field(goods, 'title')) == ('Ковер', 'Диван для отдыха'), \
        "\n[TestError][#1] -> -Failed-"
    assert tuple(i for i in field(goods, 'title', 'price')) == ({'title': 'Ковер', 'price': 2000},
                                                                {'title': 'Диван для отдыха', 'price': 5300}), \
        "\n[TestError][#2] -> -Failed-"

    print("All tests passed!\n")

    print("Run with args ('title, color'):")
    # Run
    for callback in field(goods, 'title', "color"):
        print(callback)
