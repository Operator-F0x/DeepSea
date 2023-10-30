import sys
if len(sys.argv) != 2:
    print("Usage: arping2tex <net>\n  eg: arping2tex 192.168.1.0/24")
    sys.exit(1)


from FishInTheSea import sniffer


