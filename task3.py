# Simulated internal working of dict.fromkeys()
def fromkeys(iterable, value=None):
    new_dict = {}
    for key in iterable:
        new_dict[key] = value
    return new_dict

keys = ['a', 'b', 'c']
d = fromkeys(keys, 0)
print(d)
