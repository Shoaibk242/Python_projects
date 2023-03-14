'''myseq="atgctgacatcgatatgctagcatcgatcgatcgatcgatcgatcgacatcgatcagctagcgagcatgg"
myseq=myseq.upper()
def gc_content(str):
    g=myseq.count('G')
    c=myseq.count('C')
    l=len(myseq)
    gc=((g+c)/l)*100
    return gc
print("the gc content is ",gc_content(myseq))
from Bio.Seq import Seq
from Bio.SeqUtils import GC
print (GC(myseq))
