import collections

# noinspection PyUnusedLocal
# skus = unicode string

'''
+------+-------+---------------------------------+
| Item | Price | Special offers                  |
+------+-------+---------------------------------+
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 | *
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 | *
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 | *
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 | *
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 | *
+------+-------+---------------------------------+
'''


def checkout(skus):
    if skus == '':
        return 0

    ascii_check = range(65, 115)

    result = 0

    hashtable = {
        'A': [(1, 50), (3, 130), (5, 200)], 'B': [(1, 30), (2, 45)], 'C': [(1, 20)], 'D': [(1, 15)],
        'E': [(1, 40), (2, -25)], 'F': [(1, 10), (2, -21)],
        'G': [(1, 20)], 'H': [(1, 10), (5, 45), (10, 80)], 'I': [(1, 35)], 'J': [(1, 60)], 'K': [(1, 70), (2, 120)],
        'L': [(1, 90)], 'M': [(1, 15)], 'N': [(1, 40), (3, -14)], 'O': [(1, 10)], 'P': [(1, 50), (5, 200)],
        'Q': [(1, 30), (3, 80)],
        'R': [(1, 50), (3, -10)], 'S': [(1, 20)], 'T': [(1, 20)], 'U': [(1, 40), (3, -6)],
        'V': [(1, 50), (2, 90), (3, 130)],
        'W': [(1, 20)], 'X': [(1, 17)], 'Y': [(1, 20)], 'Z': [(1, 21)]}

    place = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

    if not isinstance(skus, str) or not skus.isupper():
        return -1

    table = collections.Counter(skus)

    new_event_targets = {'S','T','X','Y','Z'}
    new_event_table = collections.defaultdict(dict)
    new_event_sum = 0

    # print(table)
    for i in sorted(table)[::-1]:
        if ord(i) not in ascii_check:
            return -1
        if i in new_event_targets:
            new_event_table[i] = table[i]
            new_event_sum += table[i]
            table[i] = 0

        while table[i] > 0:
            for cnt, price in hashtable[i][::-1]:
                mul = table[i] // cnt

                if mul > 0:
                    if price < 0:
                        cal = table[place[price]] - mul
                        if i == place[price]:
                            cal = table[place[price]] - (table[i] // (cnt + 1))

                        if cal >= 0:
                            table[place[price]] = cal
                        else:
                            table[place[price]] = 0

                        continue

                    result += (mul * price)
                    table[i] = table[i] % cnt

    if new_event_table:
        result += (new_event_sum // 3) * 45
        new_event_sum -= ((new_event_sum // 3) * 3)

        for i in new_event_table:

            if new_event_sum == 0:
                return result
            cnt, price = hashtable[i][0]

            if new_event_table[i] < new_event_sum:
                new_event_sum -= new_event_table[i]
                result += (new_event_table[i] * price)
            else:
                result += (new_event_sum * price)
                new_event_sum = 0

    return result

# print(checkout('FFFXXXXYZZZZZTTSS'))
