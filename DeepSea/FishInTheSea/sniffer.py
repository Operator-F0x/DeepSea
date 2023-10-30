from scapy.all import sniff

# Funzione di callback chiamata per ogni pacchetto catturato
def packet_callback(packet):
    print(packet.summary())  # Stampa un riassunto del pacchetto

# Cattura i pacchetti in tempo reale usando la funzione sniff()
sniff(prn=packet_callback, count=10)  # Cattura 10 pacchetti, chiamando packet_callback per ognuno


