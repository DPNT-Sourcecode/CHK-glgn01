import collections

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    ascii_check = range(65, 69)

    if not isinstance(skus, str):
        return -1

    if not skus.isupper():
        return -1
    table = collections.Counter(skus)

    for i in table:
        if ord(i) not in ascii_check:
            print(ord(i))
            return -1


    print(table)

print(checkout('ABCD'))






