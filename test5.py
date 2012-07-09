import netsnmp
from log import *

oid1 = netsnmp.VarList(netsnmp.Varbind(OID1))
res1 = netsnmp.snmpwalk(oid1, Version = 2, DestHost=IP, Community=COMMUNITY)

oid_ports = netsnmp.VarList(netsnmp.Varbind(OID_PORTS))
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

oid = netsnmp.VarList(netsnmp.Varbind(OID))
res = netsnmp.snmpwalk(oid, Version = 2, DestHost=IP, Community=COMMUNITY)

for i in range(len(res)):
    w=bin(int(res[i].encode("hex"), 16))[2:]
    if len(w)<96:
        w='0'*(96-len(w))+w
    print w

print '\n=============================================\n'

oid2 = netsnmp.VarList(netsnmp.Varbind(OID2))
res2 = netsnmp.snmpwalk(oid2, Version = 2, DestHost=IP, Community=COMMUNITY)

for i in range(len(res2)):
    ww=bin(int(res2[i].encode("hex"), 16))[2:]
    if len(ww)<96:
        ww='0'*(96-len(ww))+ww
    print ww