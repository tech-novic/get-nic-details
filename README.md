#######
get-nic
#######

Get Network Interface details such as list of interfaces, ipaddress, mac addrress, status of nic, etc. 
Currently working for Linux. 

***********
Getting Started
***********
Pip install get_nic::

 >>> pip3 install get_nic

### import::
from get_nic import getnic

# To get list of intefaces::
 >>> getnic.interfaces()

Output::
["eth0", "wlo1"]

# To get all interface details::
  >>> interfaces = getnic.interfaces()
  >>> getnic.ipaddr(interfaces)

# To get selected interface details, example lo, eth0::
 >>> interface_list = ['lo','etho']
 >>> getnic.ipaddr(interface_list)
