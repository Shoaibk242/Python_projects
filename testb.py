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
#recursive function factorial
n=input("Enter a non negative number")
n=int(n)
def factorial(x):
    if x < 1 :
        return 1
    else:
        return (x*factorial(x-1))
print("the factorial of the given number is ",factorial(n))'''
import calc
x=calc.add(6,5)
print(x)