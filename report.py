# -*- coding: utf-8 -*-
import netsnmp
import xmlrpclib
import datetime
import os
from config import *

def Report_on_switch(COMMUNITY, IP):
    '''
    Report_on_switch(COMMUNITY, IP)

    Use this function to creates a table of vlans and ports for switches. The main function.
    '''
    string = snmpw[0] + ' ' + COMMUNITY + ' ' + IP + ' ' + OID_VLANS_NAMES +' '+snmpw[1] + ' ' + out_file
    os.system(string)

    try:
        Wiki = xmlrpclib.ServerProxy(WIKI_URL)
        WikiToken = Wiki.confluence2.login(WIKI_USER, WIKI_PASS)
    except:
        if OUTPUT_TO == 'wiki':
            print 'Enter your username and password\n'
            raise

    try:
        logfile = open(out_file)
    except IOError as ErrorMess:
        print ErrorMess
        exit()

    length_logfiles = len(logfile.readlines())


    def RES(OID, snmp_request):
        '''
        RES(OID, snmp_request)

        From the value of oid returns parameters.
        '''
        try:
            if snmp_request == 'get':
                res = netsnmp.snmpget(OID, Version=2, DestHost=IP, Community=COMMUNITY)
            else:
                oid = netsnmp.VarList(netsnmp.Varbind(OID))
                res = netsnmp.snmpwalk(oid, Version=2, DestHost=IP, Community=COMMUNITY)
            if res == ():
                raise RuntimeError(err_message_snmp)
        except RuntimeError as ErrorMess:
            print ErrorMess
            exit()
        return res


    def number_of_vlan():
        '''
        number_of_vlan()

        This function returns the number of vlan.
        '''
        i = 0
        my_array = []
        logfile = open(out_file)
        while i < length_logfiles:
            x = logfile.readline()
            s = x.split(' ')
            my_array.append(s[0][28:]) #[28:] - 29 item numbers begin number of vlan
            i += 1
        return my_array


    def ports_description():
        '''
        ports_description()

        This function returns the description of port.
        '''
        list_ports_description = RES(OID_PORTS_DESCRIPTION, 'walk')
        return list_ports_description


    def HTML(array_to_html, width_array, length_array, title, number_of_vlan_array, ports_description_array):
        '''
        HTML(array_to_html, width_array, length_array, title, ports_description_array)

        This function creates a html page with a table.
        '''
        html_file = title + '.html'
        file_out = open(html_file, 'w')
        file_out.write(
            '<html><head><title>' + title +'</title>'
            '<style type="text/css">TABLE{background: #fffff0;border: 2px solid #808080;}TR.even {background: #fffacd;}'
            '</style></head><body><p align = "center"><b >' + title + ' (' + str(datetime.datetime.now())[:-7] + ')' +\
            '</b></p><table  CELLPADDING = 4 CELLSPACING = 0 border = "1"><tr class="even">\n')

        for i in range(length_array):
            if i == 1:
                for j in range(width_array + 1):
                    if j == 0: char = ' '
                    elif j == 1: char = 'Ports description '
                    else: char = '# ' + number_of_vlan_array[j - 2]
                    file_out.write('<td  align = "center">' + char + '</td>\n')
                file_out.write('</tr><tr >\n')
            for j in range(width_array):
                if j == 1:
                    char = str(ports_description_array[i - 1])
                    if i == 0: char = ' '
                    file_out.write('<td  align = "center">' + char + '</td>\n')
                if array_to_html[j][i] == '1': char = 'T'
                elif array_to_html[j][i] == '2': char = 'U'
                elif array_to_html[j][i] == '0': char = '-'
                else: char = array_to_html[j][i]
                file_out.write('<td  align = "center">' + char + '</td>\n')
            if (i % 2 == 1) or (i == 0): file_out.write('</tr><tr class="even">\n')
            else: file_out.write('</tr><tr >\n')
        file_out.write('</tr></table></body></html>')
        file_out.close()


    def WIKI(array_to_wiki, width_array, length_array, title, WikiToken, Wiki, number_of_vlan_array, ports_description_array):
        '''
        WIKI(array_to_wiki, width_array, length_array, title, WikiToken, Wiki, ports_description_array)

        This function sends the table to the specified wiki page
        and create a new page, if this page does not exist.
        '''
        content = '{wiki}\n'
        for i in range(length_array):
            if i == 1:
                for j in range(width_array + 1):
                    if j == 0: char = ' '
                    elif j == 1: char = 'Ports description '
                    else: char = '№ ' + number_of_vlan_array[j - 2]
                    content += '||' + char
                content += '|\n'
            for j in range(width_array):
                if j == 1:
                    char = str(ports_description_array[i - 1])
                    if i == 0: char = ' '
                    content += '||' + char
                if i == 0:
                    content += '||' + array_to_wiki[j][i]
                else:
                    if array_to_wiki[j][i] == '1': char = 'T'
                    elif array_to_wiki[j][i] == '2': char = 'U'
                    elif array_to_wiki[j][i] == '0': char = '-'
                    else: char = array_to_wiki[j][i]
                    if j == 0: content += '||' + char
                    else: content += '|' + char
            content += '|\n'
        content += '{wiki}'
        try:
            page = Wiki.confluence2.getPage(WikiToken, SPACE, title)
            page['content'] = ' '
            Wiki.confluence1.updatePage(WikiToken, page, {'versionComment': '', 'minorEdit': 1})
        except:
            parent = Wiki.confluence2.getPage(WikiToken, SPACE, TOP_PAGE)
            table_headers = title + '\n'
            page = {
                'parentId': parent['id'],
                'space': SPACE,
                'title': title,
                'content': table_headers + content
            }
            Wiki.confluence1.storePage(WikiToken, page)
        else:
            page = Wiki.confluence2.getPage(WikiToken, SPACE, title)
            page['content'] += content
            Wiki.confluence1.updatePage(WikiToken, page, {'versionComment': '', 'minorEdit': 1})


    title = RES(OID_SWITCH_NAME, 'get')[0]

    list_vlans_names = RES(OID_VLANS_NAMES, 'walk')
    list_ports = RES(OID_PORTS, 'walk')
    ports_numbers = list_ports

    quantity_of_ports = 0
    quantity_non_trk_ports = 0
    while list_ports[quantity_of_ports] != list_vlans_names[1]:
        quantity_of_ports += 1
        if not key_string in list_ports[quantity_of_ports]:
            quantity_non_trk_ports += 1
    quantity_non_trk_ports -= 1

    ports_numbers = ports_numbers[:quantity_of_ports - 1]

    tuple_ports = ()
    for i in range(quantity_of_ports - 1):
        string = name_port + list_ports[i]
        tuple_element = string,
        tuple_ports = tuple_ports + tuple_element

    list_ports = tuple_ports

    vlans_ports = [' '] * (len(list_vlans_names) + 1)
    for i in range(len(list_vlans_names) + 1):
        vlans_ports[i] = [' '] * (len(list_ports) + 1)

    vlans_ports[0][1:] = list_ports

    i = 1
    while i < len(list_vlans_names) + 1:
        vlans_ports[i][0] = list_vlans_names[i - 1]
        i += 1

    list_tag_vlans = RES(OID_TAG_PORTS, 'walk')

    for i in range(len(list_tag_vlans)):
        number_tag_port = bin(int(list_tag_vlans[i].encode('hex'), 16))[2:]
        if len(number_tag_port) < quantity_non_trk_ports * 2:
            number_tag_port = '0' * (quantity_non_trk_ports * 2 - len(number_tag_port)) + number_tag_port
        vlans_ports[i + 1][1:] = number_tag_port

    list_untag_vlans = RES(OID_UNTAG_PORTS, 'walk')

    for i in range(len(list_untag_vlans)):
        number_untag_port = bin(int(list_untag_vlans[i].encode('hex'), 16))[2:]
        if len(number_untag_port) < quantity_non_trk_ports * 2:
            number_untag_port = '0' * (quantity_non_trk_ports * 2 - len(number_untag_port)) + number_untag_port
        for j in range(len(number_untag_port)):
            if number_untag_port[j] == '1': vlans_ports[i + 1][j + 1] = '2'

    array_ports_numbers = []
    for i, port_number in enumerate(ports_numbers):
        if not key_string in ports_numbers[i]:
            array_ports_numbers.append(int(port_number))
            last_port_number = int(port_number)
        else:
            array_ports_numbers.append(last_port_number + int(port_number[3:]))

    i = 1
    while i < len(list_vlans_names) + 1:
        j = 1
        while j < len(ports_numbers) + 1:
            vlans_ports[i][j] = vlans_ports[i][array_ports_numbers[j - 1]]
            j += 1
        i += 1

    if OUTPUT_TO == 'wiki':
        WIKI(vlans_ports, len(list_vlans_names) + 1, len(list_ports) + 1, title, WikiToken, Wiki, number_of_vlan(),
            ports_description())
    else:
        HTML(vlans_ports, len(list_vlans_names) + 1, len(list_ports) + 1, title, number_of_vlan(), ports_description())


for i in range(len(switches)):
    Report_on_switch(switches[i]['COMMUNITY'], switches[i]['IP'])
