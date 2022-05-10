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
        'A':[(1, 50), (3, 130), (5, 200)], 'B': [(1, 30), (2, 45)], 'C': [(1, 20)], 'D': [(1, 15)], 'E': [(1, 40), (2, -4)]
    }

    if not isinstance(skus, str) or not skus.isupper():
        return -1

    table = collections.Counter(skus)

    for i in sorted(table)[::-1]:
        if ord(i) not in ascii_check:
            return -1

        while table[i] > 0:
            for cnt, price in hashtable[i][::-1]:
                mul = table[i] // cnt

                if mul > 0:
                    if price < 0:
                        cal = table[price] - mul
                        if  cal >= 0:
                            table[price] = cal
                        else:
                            table[price] = 0

                        continue
                    print(i)

                    result += (mul * price)
                    table[i] = table[i] % cnt

    return result


print(checkout('ABBBBBBCDDEEEEEEEEEEEE'))

# - {"method": "checkout", "params": ["AAAAA"], "id": "CHK_R2_017"}, expected: 200, got: 230
# - {"method": "checkout", "params": ["AAAAAA"], "id": "CHK_R2_018"}, expected: 250, got: 260
# - {"method": "checkout", "params": ["AAAAAAA"], "id": "CHK_R2_019"}, expected: 300, got: 310
#




