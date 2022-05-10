# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    check_volume = range(100)

    if x not in check_volume and y not in check_volume:
        raise Exception("check the value - x : {}, y : {}".format(x, y))

    result = x + y

    return x + y
