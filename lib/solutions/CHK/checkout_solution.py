import collections

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    
    if not skus.isupper():
        return -1

    table = collections.Counter(skus)
    print(table)

print(checkout('AB*'))




