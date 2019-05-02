Usage:

1. import the class, initialize an instance of the socket as either a 'pi' or 'laptop'
2. send strings in a synchronous manner with send
3. recieve strings in a synchronous manner with recieve

to set up raspi connection to pc:
connect raspberry pi to ethernet port with a cat-5 cable
go into your network ipv4 settings on your laptop for your ethernet interface, and change it from DHCP to Shared with other computers
check the raspberry pi now has an internet connection via your computer

if you set up with type 'laptop' the init process automatically runs a command to find your raspberry pi by mac address