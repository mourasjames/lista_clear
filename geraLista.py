#!/usr/bin/python3 
# -*- coding: UTF-8 -*-

mod_cmts = input("Informe o VENDOR (Motorola, Cisco, Arris, Casa):  " )

mod_cmts = mod_cmts.upper()


if mod_cmts == "MOTOROLA":
    
    temp = open("lista_macs.txt", "r")
    linha = temp.readlines()
    for i in  linha:
        print("clear cable modem {}.{}.{} reset \n".format(i[:4], i[4:8], i[8:12]))
    temp.close()
    
elif mod_cmts == "CISCO":
    
    temp = open("lista_macs.txt", "r")
    linha = temp.readlines()
    for i in  linha:
        print("clear cable modem {}.{}.{} delete".format(i[:4], i[4:8], i[8:12]))
    temp.close()
    
elif mod_cmts == "ARRIS":
    
    temp = open("lista_macs.txt", "r")
    linha = temp.readlines()
    for i in  linha:
        print("clear cable modem {}.{}.{} delete".format(i[:4], i[4:8], i[8:12]))
    temp.close()
    
elif mod_cmts == "CASA":
    
    temp = open("lista_macs.txt", "r")
    linha = temp.readlines()
    for i in  linha:
        print("clear cable modem {}.{}.{} reset".format(i[:4], i[4:8], i[8:12]))
    temp.close()
