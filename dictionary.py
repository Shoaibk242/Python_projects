l1=["two","three","four"]
l2=[2,3,4]
dict={}
print(dict)
for k in l1:
    for v in l2:
        dict[k] = v
        l2.remove(v)
        break
print(dict)
print(dict['2'])
