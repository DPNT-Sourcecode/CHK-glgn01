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
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
+------+-------+------------------------+
'''

def checkout(skus):

    if skus == '':
        return 0

    ascii_check = range(65, 71)

    result = 0

    hashtable = {
        'A':[(1, 50), (3, 130), (5, 200)], 'B': [(1, 30), (2, 45)], 'C': [(1, 20)], 'D': [(1, 15)], 'E': [(1, 40), (2, -25)], 'F' : [(1, 10), (2, -21)]
    }
    place = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

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
                        cal = table[place[price]] - mul
                        if i == place[price]:
                            cal = mul + 1

                        if  cal >= 0:
                            table[place[price]] = cal
                        else:
                            table[place[price]] = 0

                        continue

                    result += (mul * price)
                    table[i] = table[i] % cnt

    return result


# print(checkout('FFFF'))



