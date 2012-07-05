import netsnmp

oid1 = netsnmp.VarList(netsnmp.Varbind('.1.3.6.1.2.1.17.7.1.4.3.1.1'))
#oid = netsnmp.VarList(netsnmp.Varbind('.1.3.6.1.2.1.17.7.1.4.3.1.2'))
#oid = netsnmp.VarList(netsnmp.Varbind('.1.3.6.1.2.1.17.7.1.4.3.1.4'))
oid2 = netsnmp.VarList(netsnmp.Varbind('.1.3.6.1.2.1.47.1.1.1.1.7'))


res1 = netsnmp.snmpwalk(oid1, Version = 2, DestHost='172.18.82.20', Community='test2012')
res2 = netsnmp.snmpwalk(oid2, Version = 2, DestHost='172.18.82.20', Community='test2012')

#print res

i=0
while i<len(res1):
    print res1[i]
    i+=1

print "\n-------------1--------------\n"

res3=[]
res3=res2
i=0
res2=[]
while i<len(res3):
    res2[i]=res3[i]
    print res2[i]
    i+=1

print "\n-------------2--------------\n"

i=0
while i<len(res2):
    print res2[i]
    i+=1

print "\n-------------3--------------\n"

'''
A = []
A = [0] * (len(res1)+1)
for i in range(len(res1)+1):
    A[i] = [0] * (len(res2)+1)

print '>>>>>>>>>>>>>>',len(A)

for i in range(len(res1)+1):
    if i==0:
        A[i]=res2
    #else:A[i][0]=res1[i]

print '>>>>>>>>>>>>>>',len(A)

for i in range(len(res1)+1):
    for j in range(len(res2)+1):
        print A[i][j],' '
    print "\n"
'''