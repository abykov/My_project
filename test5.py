import netsnmp


oid = netsnmp.VarList(netsnmp.Varbind('.1.3.6.1.2.1.17.7.1.4.3.1.2'))
oid1 = netsnmp.VarList(netsnmp.Varbind('.1.3.6.1.2.1.17.7.1.4.3.1.1'))
#oid = netsnmp.VarList(netsnmp.Varbind('.1.3.6.1.2.1.17.7.1.4.3.1.4'))
oid2 = netsnmp.VarList(netsnmp.Varbind('.1.3.6.1.2.1.47.1.1.1.1.7'))


res1 = netsnmp.snmpwalk(oid1, Version = 2, DestHost='172.18.82.20', Community='test2012')
res2 = netsnmp.snmpwalk(oid2, Version = 2, DestHost='172.18.82.20', Community='test2012')


res2=res2[9:]

A = []
A = [0] * (len(res1)+1)
for i in range(len(res1)+1):
    A[i] = [0] * (len(res2)+1)

A[0][1:]=res2

i=1
while i<len(res1)+1:
    A[i][0]=res1[i-1]
    i+=1

#for i in range(len(res1)+1):
#        print A[i]

res = netsnmp.snmpwalk(oid, Version = 2, DestHost='172.18.82.20', Community='test2012')
print res

for i in range(len(res)):
    #print bin(int(res[i], 16))[2:]
    print 'str',res[i]

s=str(res[1])
print 'len ',len(s), 's1', s[1]
#s.replace(' ' ,'')


#print s



