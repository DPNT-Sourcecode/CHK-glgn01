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
        'A': 50, 'AAA' : 130, 'B': 30, 'BB' : 45, 'C': 20, 'D': 15
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
        print(table)
        if i == 'A':
            mul, res = divmod(table[i], 3)
            if mul > 0:
                result += (mul * hashtable[i * 3])
            if res > 0:
                result += (res * hashtable[i])

        elif i == 'B':
            mul, res = divmod(table[i], 2)
            if mul > 0:
                result += (mul * hashtable[i*2])
            if res > 0:
                result += (res * hashtable[i])

        else:
            result += hashtable[i]

    return result

print(checkout('AAAAAAABBCCD'))








