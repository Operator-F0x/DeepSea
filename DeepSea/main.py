print("""                                                           
,------.                            ,---.                  
|  .-.  \  ,---.  ,---.  ,---.     '   .-'  ,---.  ,--,--. 
|  |  \  :| .-. :| .-. :| .-. |    `.  `-. | .-. :' ,-.  | 
|  '--'  /\   --.\   --.| '-' '    .-'    |\   --.\ '-'  | 
`-------'  `----' `----'|  |-'     `-----'  `----' `--`--' 
                        `--'                               
      by Saywoc""")

import sys
if len(sys.argv) != 2:
    print("Usage: main.py <argument>\n  main.py eg: -H for help")
    sys.exit(1)

if sys.argv[1] == '-h' or '-H':
    print("-SN ipv4 10 : <sniff 10 live packet>\n" 
          "-SN ipv4 L  : <sniff live packet 'Til you stop it>\n\n"
          "-RT         : <show the route table>")


from scapy.all import *
from FishInTheSea import sniffer

if sys.argv[1] == "-SN":

sniffer.scapysniff(sys.argv[2], sys.argv[3])



print(Route())