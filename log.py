switches = [
        {'IP': '172.18.82.20',
         'COMMUNITY': 'test2012'},
        {'IP': '172.18.146.4',
         'COMMUNITY': 'test2012'},
]
#IP = '172.18.82.20'
#IP = '172.18.146.4'
#COMMUNITY = 'test2012'

OID_PORTS = '.1.3.6.1.2.1.2.2.1.2'
OID_TAG_PORTS = '.1.3.6.1.2.1.17.7.1.4.3.1.2' #tagged vlan
OID_VLANS_NAMES = '.1.3.6.1.2.1.17.7.1.4.3.1.1'
OID_UNTAG_PORTS = '.1.3.6.1.2.1.17.7.1.4.3.1.4' #untagged vlan
OID_SWITCHE_NAMES = '.1.3.6.1.2.1.1.1.0'

key_string = 'Trk'
name_port = 'Port '
out_file = 'log.dat'
name_html_file = 'Table.html'
snmpw = 'snmpwalk -v2c -c '
title = 'Table'