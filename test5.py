import netsnmp
import os
from log import *


string='snmpwalk -v2c -c '+COMMUNITY+' '+IP+' '+OID1+'  > log.dat'
os.system(string)
file=open('log.dat')


N=len(file.readlines())

def HTML(b,M,N):
    f_out=open('Table.html','w')
    f_out.write('<html><head><title>Table </title></head><body><p>Table.</p><table border="1"><tr>\n')
    for i in range(N):
        for j in range(M):
            if b[j][i]=='1':
                d='X'
            elif b[j][i]=='0':d="O"
            else:d=b[j][i]
            f_out.write('<td align="center">'+d+'</td>\n')
        f_out.write('</tr><tr>\n')
    f_out.write('</tr></table></body></html>')
    f_out.close()


def number_of_vlan(j):
    i=0
    A=[]
    file=open('log.dat')
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
A = ['0'] * (len(res1)+1)
for i in range(len(res1)+1):
    A[i] = ['0'] * (len(res_ports)+1)

A[0][1:]=res_ports


i=1
while i<len(res1)+1:
    A[i][0]=res1[i-1]+' '+number_of_vlan(i-1)
    i+=1


res=RES(OID)

for i in range(len(res)):
    w=bin(int(res[i].encode("hex"), 16))[2:]
    if len(w)<96:
        w='0'*(96-len(w))+w
    A[i+1][1:]=w[:48]
    print w

print '\nsssssssssssssssssssssssssssss\n'

res2 = RES(OID2)

for i in range(len(res2)):
    ww=bin(int(res2[i].encode("hex"), 16))[2:]
    if len(ww)<96:
        ww='0'*(96-len(ww))+ww
    print ww


HTML(A,len(res1)+1,len(res_ports)+1)
