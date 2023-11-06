import logging
logging.getLogger("scapy").setLevel(logging.CRITICAL)

from scapy.all import *

# Funzione di callback chiamata per ogni pacchetto catturato
def packet_callback(packet):
    print(packet.summary())  # Stampa un riassunto del pacchetto

def scapysniff(packet_Number: int):
    #Cattura i pacchetti in tempo reale usando la funzione sniff()
    sniff(prn=packet_callback, count=packet_Number) 

#debug call
#scapysniff(40)