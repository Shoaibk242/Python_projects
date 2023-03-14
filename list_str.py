def uncommon(la,lb):
    lc=[]
    for x in la:
        if x not in lb:
            lc+=[x]
    for i in lb:
        if i not in la:
            lc+=[i]
    return lc
color_list_1 = ["White", "Black", "Red"]
color_list_2 =["Red", "Green"]
print(uncommon(color_list_2,color_list_1))