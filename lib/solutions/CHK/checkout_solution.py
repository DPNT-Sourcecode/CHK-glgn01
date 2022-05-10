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
        'A':[(1, 50), (3, 130), (5, 200)], 'B': [(1, 30), (2, 45)], 'C': [(1, 20)], 'D': [(1, 15)], 'E': [(1, 40)]
    }

    if not isinstance(skus, str) or not skus.isupper():
        return -1

    table = collections.Counter(skus)

    for i in sorted(table)[::-1]:
        if ord(i) not in ascii_check:
            return -1

        while table[i] > 0:
            print(table)
            for cnt, price in hashtable[i][::-1]:
                mul, res = table[i] // cnt

                if mul > 0:
                    if i == 'E':
                        cal = table['B'] - mul
                        if  cal >= 0:
                            table['B'] = cal
                        else:
                            table['B'] = 0

                    result += (mul * price)

                else:
                    if res > 0:
                        result += (res * price)
                table[i] = res

        print(divmod(1, 5))

        # elif i == 'E':
        #     mul, res = divmod(table[i], 2)
        #
        #     if mul > 0:
        #         cal = table['B'] - mul
        #         if  cal >= 0:
        #             table['B'] = cal
        #         else:
        #             table['B'] = 0
        #
        #     result += (table[i] * hashtable[i])
        #
        # else:
        #     result += (hashtable[i] * table[i])

    return result


print(checkout('ABBBBBBCDDEEEEEEEEEEEE'))

# - {"method": "checkout", "params": ["AAAAA"], "id": "CHK_R2_017"}, expected: 200, got: 230
# - {"method": "checkout", "params": ["AAAAAA"], "id": "CHK_R2_018"}, expected: 250, got: 260
# - {"method": "checkout", "params": ["AAAAAAA"], "id": "CHK_R2_019"}, expected: 300, got: 310
#

