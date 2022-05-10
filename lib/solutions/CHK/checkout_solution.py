import collections

# noinspection PyUnusedLocal
# skus = unicode string

'''
+------+-------+------------------------+
| Item | Price | Special offers         |
+------+-------+------------------------+
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
+------+-------+------------------------+
'''

def checkout(skus):

    if skus == '':
        return 0

    ascii_check = range(65, 70)

    result = 0

    hashtable = {
        'A': 50, 'AAA' : 130, 'AAAAA' : 200,'B': 30, 'BB' : 45, 'C': 20, 'D': 15, 'E': 40
    }

    if not isinstance(skus, str) or not skus.isupper():
        return -1

    table = collections.Counter(skus)

    for i in sorted(table)[::-1]:
        if ord(i) not in ascii_check:
            return -1

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

        elif i == 'E':
            mul, res = divmod(table[i], 2)

            if mul > 0:
                cal = table['B'] - mul
                if  cal >= 0:
                    table['B'] = cal
                else:
                    table['B'] = 0

            result += (table[i] * hashtable[i])

        else:
            result += (hashtable[i] * table[i])

    return result


print(checkout('ABBBBBBCDDEEEEEEEEEEEE'))

- {"method": "checkout", "params": ["AAAAA"], "id": "CHK_R2_017"}, expected: 200, got: 230
- {"method": "checkout", "params": ["AAAAAA"], "id": "CHK_R2_018"}, expected: 250, got: 260
- {"method": "checkout", "params": ["AAAAAAA"], "id": "CHK_R2_019"}, expected: 300, got: 310






