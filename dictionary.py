"""
Write a function dict_merge_sum that takes two dictionaries d1 and d2 as parameters. 
The values of both dictionaries are numerical. The function should return the merged sum dictionary m of those dictionaries. 
If a key k is both in d1 and d2, the corresponding values will be added and included in the dictionary m. If k is only contained in one of the dictionaries,
the k and the corresponding value will be included in m

"""

def dict_merge_sum(d1:dict,d2:dict) -> dict:
    merged_dict = {}

    for key,value in d1.items():
        merged_dict[key] = merged_dict.get(key, 0) + int(value)

    for key,value in d2.items():
        merged_dict[key] = merged_dict.get(key, 0) + int(value)

    return merged_dict
    



d1 = {'a':'1','b':'2','c':'3'}
d2 = {'a':'4','d':'5','e':'6'}
merged_sum = dict_merge_sum(d1,d2)
print(merged_sum)
