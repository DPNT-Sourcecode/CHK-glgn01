import collections

# noinspection PyUnusedLocal
# skus = unicode string

'''
+------+-------+----------------+
| Item | Price | Special offers |
+------+-------+----------------+
| A    | 50    | 3A for 130     |
| B    | 30    | 2B for 45      |
| C    | 20    |                |
| D    | 15    |                |
+------+-------+----------------+
'''
def checkout(skus):
    ascii_check = range(65, 69)

    result = 0

    hashtable = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15
    }

    if not isinstance(skus, str):
        return -1

    if not skus.isupper():
        return -1
    table = collections.Counter(skus)

    for i in table:
        if ord(i) not in ascii_check:
            print(ord(i))
            return -1

        if i == 'A':
            print(divmod(table[i], 3))

        # elif == 'B':
        #     pass
        # else:
        #     pass






print(checkout('AAAABC'))









