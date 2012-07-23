switches = [
        {'IP': '172.18.82.20',      #sar02-7-asw01
        'COMMUNITY': 'test2012'},

        {'IP': '172.18.146.4',         #spb04-1-sw
        'COMMUNITY': 'test2012'},

        {'IP': '172.18.146.6',         #spb04-1-sw3
        'COMMUNITY': 'test2012'},
           ]

OID_PORTS = '.1.3.6.1.2.1.2.2.1.2'
OID_TAG_PORTS = '.1.3.6.1.2.1.17.7.1.4.3.1.2'   #tagged ports
OID_UNTAG_PORTS = '.1.3.6.1.2.1.17.7.1.4.3.1.4' #untagged ports
OID_VLANS_NAMES = '.1.3.6.1.2.1.17.7.1.4.3.1.1'
OID_SWITCH_NAME = '.1.3.6.1.2.1.1.5.0'

WIKI_USER = ''
WIKI_PASS = ''
WIKI_URL = 'https://wiki.griddynamics.net/rpc/xmlrpc'
SPACE = 'SP'
TOP_PAGE = 'abykov'

err_message_snmp = 'SNMP has returned zero bytes.'
err_message_wiki = 'Such a table already exists in the wiki\n'
key_string = 'Trk'
name_port = 'Port '
out_file = 'log.dat'
snmpw = 'snmpwalk -v2c -c '

OUTPUT_TO = 'html'      #OUTPUT_TO = 'wiki' if you want to send the table into the specified wiki page,
                        #OUTPUT_TO = 'html' send the table to html page
