```
from scapy.all import *
import random,string

for i in range(5):
        trame = Ether()
        trame.dst = 'ff:ff:ff:ff:ff:ff'
        MAC_src_fake_list = [''.join(random.choice('abcdef' + string.digits) for _ in range(2)) for i in range(6)]
        trame.src = ':'.join(MAC_src_fake_list)
        sendp(trame)
```        
