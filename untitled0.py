
import itertools
List=raw_input("Enter Your List please :")
l1=len(List)
a=list(itertools.permutations(List))
n=len(a)
toprow=[]
for i in List:
    toprow.append(i)
toprow=tuple(toprow)
print "\n OUTPUT\n"
for i in range(n):
    print "A",i+1,"=",toprow,"\n     ",a[i],"\n"
  

def func(a1, a2,a,l1,list):
    b1=[]
    for i in range(0,l1):              
        b1.append(0)
    for i in range(l1):                   
        x=a2[i]
        for j in range(l1):
            if x==list[j]:
                break
        b1[i]=a1[j]                     
    b1=tuple(b1)
    for m in range(n):
        if b1==a[m]:
            break    
    return m
            
print "\t",
for i in range(n):
   print "A",i+1,"\t",                #printing heading for table
print "\n\t",

for i in range(n):                    #underline for headings
   print "___\t",
   
   
print "\n"
for i in range(n):
   print "A",i+1,"|\t",                   #print left index for table
   for j in range(n):
       m=func(a[i],a[j],a,l1,List)
       print "A",m+1,"\t",
       #print b,
       
   print "\n"





