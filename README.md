# falcon_cisco
Gets device list from cisco with ssh connection and return as an web service.

The program has been created for get devices informations from CISCO interface and parse it to JSON format and serve it as a webservice over falcon framework.

Endpoints of this app is doing,

-findalldevices -> returns all devices that connected on network
-findsingledevice -> returns single device with sended macaddress that connected on network
-findmultipledevices -> returns single device with sended macaddresses that connected on network