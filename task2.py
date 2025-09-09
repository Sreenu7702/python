# Simulated internal behavior for sort(key=len)
def sort_by_len(lst):
    decorated = [(len(item), item) for item in lst]
    decorated.sort(key=lambda x: x[0])
    for i in range(len(lst)):
        lst[i] = decorated[i][1]

data = ["apple", "kiwi", "banana", "fig"]
sort_by_len(data)
print(data)

# Internal working of list.clear()
def list_clear(lst):
    del lst[:]
my_list = [1, 2, 3]
list_clear(my_list)
print(my_list)

# Internal working of dict.clear()
def dict_clear(dct):
    for key in list(dct.keys()):
        del dct[key]
my_dict = {"a": 1, "b": 2}
dict_clear(my_dict)
print(my_dict)
