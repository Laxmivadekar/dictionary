def dict_merge_sum(d1, d2):
    merged_sum = d1.copy()
    for key, value in d2.items():
        if key in d1:
            d1[key] += value
        else:
            d2[key] = value
    
    print(merged_sum)

d1 = dict(a=4, b=5, d=8)
d2 = dict(a=1, d=10, e=9)

dict_merge_sum(d1, d2)