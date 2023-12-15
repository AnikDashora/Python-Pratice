f = open("JTOI.txt","w")
f.write("WELL, THJS JS A WORD BY JTSELF. YOU COULD STRETCH THJS TO BE A SENTENCE")
f.close()

f = open("JTOI.txt","r")
x = f.read()
import re
x = re.sub("J","I",x)
print(x)
f.close()

f = open("JTOI.txt","w")
f.write(x)