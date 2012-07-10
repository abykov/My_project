import netsnmp
from log import *

def RES(OID):
    oid = netsnmp.VarList(netsnmp.Varbind(OID))
    res = netsnmp.snmpwalk(oid, Version = 2, DestHost=IP, Community=COMMUNITY)
    return res


res1 = RES(OID1)
res_ports = RES(OID_PORTS)

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

res=RES(OID)

for i in range(len(res)):
    w=bin(int(res[i].encode("hex"), 16))[2:]
    if len(w)<96:
        w='0'*(96-len(w))+w
    print w

print '\n=============================================\n'

res2 = RES(OID2)

for i in range(len(res2)):
    ww=bin(int(res2[i].encode("hex"), 16))[2:]
    if len(ww)<96:
        ww='0'*(96-len(ww))+ww
    print ww

#for i in range(len(res_ports)):
#    print ww[i*2],' ',ww[i*2+1]