# get-nic-details
Get Network Interface details

### Getting started
pip3 install get_nic

from get_nic import getnic

# To get list of intefaces
getnic.interfaces()

Output:
["eth0", "wlo1"]

# To get all interface details
>>>interfaces = getnic.interfaces()
>>>getnic.ipaddr(interfaces)

# To get selected interface details, example lo, eth0
>>>interface_list = ['lo','etho']
>>>getnic.ipaddr(interface_list)
