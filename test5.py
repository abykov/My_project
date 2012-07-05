import netsnmp

oid = netsnmp.VarList(netsnmp.Varbind('.1.3.6.1.2.1.17.7.1.4.3.1.1'))
#oid = netsnmp.VarList(netsnmp.Varbind('.1.3.6.1.2.1.17.7.1.4.3.1.2'))
#oid = netsnmp.VarList(netsnmp.Varbind('.1.3.6.1.2.1.17.7.1.4.3.1.4'))
res = netsnmp.snmpwalk(oid, Version = 2, DestHost='172.18.82.20', Community='test2012')

print res




