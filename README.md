# get-nic


Get Network Interface details such as list of interfaces, ipaddress, mac addrress, status of nic, etc. 
Currently working for Linux. 

## Get Started


Pip install get_nic::

   >>> pip3 install get_nic


### import
import module::
   >>> from get_nic import getnic

### To get list of intefaces
Get list of network interfaces::
   >>> getnic.interfaces()

Output
["eth0", "wlo1"]

### To get all interface details
From the interface list get details of all the interfaces::
   >>> interfaces = getnic.interfaces()
   >>> getnic.ipaddr(interfaces)

### To get selected interface details, example lo, eth0
Pass interface names in a list::
   >>> interface_list = ['lo','etho']
   >>> getnic.ipaddr(interface_list)
