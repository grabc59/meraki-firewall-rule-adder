A python tool to add layer 3 outbound rules to a Meraki MX firewall network.

The tool will prompt for API key, org, and network ID. 
It will read from rules.txt. 
It expects a list of IPs, one per line in the rules.txt file. 
It appends a /32 to each IP and pushes them simultaneously. 
