print("""                                                           
,------.                            ,---.                  
|  .-.  \  ,---.  ,---.  ,---.     '   .-'  ,---.  ,--,--. 
|  |  \  :| .-. :| .-. :| .-. |    `.  `-. | .-. :' ,-.  | 
|  '--'  /\   --.\   --.| '-' '    .-'    |\   --.\ '-'  | 
`-------'  `----' `----'|  |-'     `-----'  `----' `--`--' 
                        `--'                               
      by Saywoc\n""")
import sys
from scapy.all import *
from FishInTheSea import sniffer

if len(sys.argv) != 2:
    print("\nUsage: main.py <argument>\n  main.py eg: -H for help")
    sys.exit(1)

if sys.argv[1] == '-H':
    print("\n-SN 10 : <sniff 10 live packet on localhost>\n" 
          "-R         : <show the route table>")

if sys.argv[1] == '-SN':
    packet_number = 5 
    sniffer.scapysniff(packet_number)
    sys.exit(0)

if sys.argv[1] == '-R':    
    print(Route())
    sys.exit(0)