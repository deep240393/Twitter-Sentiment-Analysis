
list1=["not safe"," safe "," accident ","long waiting"," expensive "," friendly ","snow storm","good school","bad school","poor school",
" immigrants "," immigrant "," parking "," pollution "," parks "," park "," bus "," buses "]

p1=[]

distFile = sc.textFile("mapreduce_in.txt")
c=0
for i in distFile.take(1500):
    for j in range(len(list1)):
        if list1[j].lower() in i.lower():
            
            if (list1[j]==" safe "):
                if ("not safe" in i.lower()):
                    continue
	    if (list1[j]=="poor school"):
	    	p1.append("bad school") 
		continue
	    if (list1[j]==" immigrants "):
	    	p1.append(" immigrant ") 
		continue
            if (list1[j]==" buses "):
	    	p1.append(" bus ") 
		continue
            p1.append(list1[j])
                     

print(p1) 
mapping = map((lambda x : (x, 1)), p1)
sorted_mapping = sorted(mapping)
print(sorted_mapping)
from itertools import groupby
grouper = groupby(sorted_mapping, lambda p:p[0])
list2=(map(lambda l: (l[0], reduce(lambda x, y: x + y, map(lambda p:p[1], l[1]))), grouper))
print(list2)

list3=[]

for i in list2:
    list3.append(i[0]+" " +str(i[1]))

    
string1=" "

    
for i in list3:
    string1 = string1 + "\n"+ i


print(string1)


file = open('test.txt','w')
file.write(string1)
file.close()
