f = open(r'./bookcomment.txt','r')
line=f.readline()
tet='123\n'
while line:
    #print line,
    tet = tet + line
    line = f.readline()
f.close()
print tet