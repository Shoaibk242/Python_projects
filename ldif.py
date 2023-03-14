l1=[1,2,3,7,8,12,45,9,78,12]
l2=[1,2,3,4,5,6,7,988,9]
def uncommon(la,lb):
    lc=[]
    for x in la:
        if x not in lb:
            lc+=[x]
    for i in lb:
        if i not in la:
            lc+=[i]
    return lc
def common(la,lb):
    lc=[]
    for x in la:
        if x in lb:
            lc+=[x]
    return lc
print("uncommon elements ",uncommon(l1,l2))
print("common elements ",common(l1,l2))