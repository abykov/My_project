# -*- coding: utf-8 -*-
import netsnmp
import os
from log import *

def Report_on_switche(COMMUNITY, IP, html_file):
    '''Creates a table of vlans and ports for switches'''
    string = snmpw + ' ' + COMMUNITY + ' ' + IP + ' ' + OID_VLANS_NAMES + ' > ' + out_file
    os.system(string)
    logfile = open(out_file)

    length_logfiles = len(logfile.readlines())


    def RES(OID):
        '''From the value of oid returns parameters'''
        oid = netsnmp.VarList(netsnmp.Varbind(OID))
        res = netsnmp.snmpwalk(oid, Version=2, DestHost=IP, Community=COMMUNITY)
        return res


    def HTML(array_to_print, width_array, length_array):
        '''Creates a html page with a table '''
        file_out = open(html_file, 'w')
        file_out.write(
            '<html><head><title>' + title + '</title></head><body><p align = "center"><b >' + title + '</b></p>'
            '<table  CELLPADDING = 4 CELLSPACING = 0 border = "1"><tr >\n')
        for i in range(length_array):
            for j in range(width_array):
                if array_to_print[j][i] == '1': char = 'T'
                elif array_to_print[j][i] == '2': char = 'U'
                elif array_to_print[j][i] == '0': char = "-"
                else: char = array_to_print[j][i]
                file_out.write('<td  align = "center">' + char + '</td>\n')
            file_out.write('</tr><tr >\n')
        file_out.write('</tr></table></body></html>')
        file_out.close()


    def number_of_vlan(number):
        '''Returns the number of network'''
        i = 0
        array = []
        logfile = open(out_file)
        while i < length_logfiles:
            x = logfile.readline()
            s = x.split(' ')
            array.append(s[0][29:])
            i += 1
        return array[number]


    list_vlans_names = RES(OID_VLANS_NAMES)
    list_ports = RES(OID_PORTS)
    ports_numbers = list_ports

    quantity_of_ports = 0
    while list_ports[quantity_of_ports] != list_vlans_names[1]:
        quantity_of_ports += 1

    ports_numbers = ports_numbers[:quantity_of_ports - 1]

    tuple_ports = ()
    for i in range(quantity_of_ports - 1):
        string = name_port + list_ports[i]
        tuple_element = string,
        tuple_ports = tuple_ports + tuple_element

    list_ports = tuple_ports

    vlans_ports = ['0'] * (len(list_vlans_names) + 1)
    for i in range(len(list_vlans_names) + 1):
        vlans_ports[i] = ['0'] * (len(list_ports) + 1)

    vlans_ports[0][1:] = list_ports

    i = 1
    while i < len(list_vlans_names) + 1:
        vlans_ports[i][0] = list_vlans_names[i - 1] + ' ' + number_of_vlan(i - 1)
        i += 1

    list_tag_vlans = RES(OID_TAG_PORTS)

    for i in range(len(list_tag_vlans)):
        number_teg_port = bin(int(list_tag_vlans[i].encode('hex'), 16))[2:]
        if len(number_teg_port) < 96:
            number_teg_port = '0' * (96 - len(number_teg_port)) + number_teg_port
        vlans_ports[i + 1][1:] = number_teg_port

    list_untag_vlans = RES(OID_UNTAG_PORTS)

    for i in range(len(list_untag_vlans)):
        number_unteg_port = bin(int(list_untag_vlans[i].encode('hex'), 16))[2:]
        if len(number_unteg_port) < 96:
            number_unteg_port = '0' * (96 - len(number_unteg_port)) + number_unteg_port
        j = 0
        for j in range(len(number_unteg_port)):
            if number_unteg_port[j] == '1': vlans_ports[i + 1][j + 1] = '2'

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

    HTML(vlans_ports, len(list_vlans_names) + 1, len(list_ports) + 1)


for i in range(len(switches)):
    Report_on_switche(switches[i]['COMMUNITY'], switches[i]['IP'], str(i + 1) + '_' + name_html_file)
