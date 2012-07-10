import netsnmp
import os
from log import *

os.system('snmpwalk -v2c -c test2012 172.18.82.20 .1.3.6.1.2.1.17.7.1.4.3.1.1 > qwe.dat')
file=open('qwe.dat')
N=len(file.readlines())


def number_of_vlan(j):
    i=0
    A=[]
    file=open('qwe.dat')
    while i<N:
        x=file.readline()
        s=x.split(' ')
        A.append(s[0][29:])
        i+=1
    return A[j]


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
    A[i][0]=res1[i-1]+' '+number_of_vlan(i-1)
    i+=1



for i in range(len(res1)+1):
    print A[i]

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