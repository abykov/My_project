import netsnmp
from log import *



oid = netsnmp.VarList(netsnmp.Varbind(OID))
oid1 = netsnmp.VarList(netsnmp.Varbind(OID1))
#oid2 = netsnmp.VarList(netsnmp.Varbind(OID2))
oid_ports = netsnmp.VarList(netsnmp.Varbind(OID_PORTS))


res1 = netsnmp.snmpwalk(oid1, Version = 2, DestHost=IP, Community=COMMUNITY)
res_ports = netsnmp.snmpwalk(oid_ports, Version = 2, DestHost=IP, Community=COMMUNITY)

res_ports=res_ports[9:]

A = []
A = [0] * (len(res1)+1)
for i in range(len(res1)+1):
    A[i] = [0] * (len(res_ports)+1)

A[0][1:]=res_ports

i=1
while i<len(res1)+1:
    A[i][0]=res1[i-1]
    i+=1


res = netsnmp.snmpwalk(oid, Version = 2, DestHost=IP, Community=COMMUNITY)

for i in range(len(res)):
    w=bin(int(res[i].encode("hex"), 16))[2:]
    print i,') len',len(w),'  ',w

