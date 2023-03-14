seq="AUGCAUGC"
seq=seq.replace("A","T")
seq=seq.replace("U","A")
seq1=list(seq)
for x in range(0,len(seq1)):
    i=seq1.index("G")
    print (i)
    seq1.pop(i)
    '''seq=seq.insert[i,'C']'''
    '''elif (x=="C"):
     x=seq.index("C")
     print(x)
     seq=seq.pop(x)
     seq=seq.insert(x,"G")  
    else:
     pass'''     
print(seq1)