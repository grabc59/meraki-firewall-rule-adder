import requests
from prettytable import PrettyTable
from meraki import meraki

# get API key
apikey = input(f'-> Enter your API key: ')
base_url = 'https://api.meraki.com/api/v0'
myOrgs = meraki.myorgaccess(apikey)

# print the orgs to select from
orgs_table = PrettyTable(field_names=["ID", "Org name"])
for org in myOrgs:
    orgs_table.add_row([org["id"], org["name"]])
print(orgs_table)

# get org ID
print('-> Enter the organization ID that contains the network to which we will add firewall rules.')
org_id = input(f'Org ID: ')

# get a list of networks in the organization
network_list = meraki.getnetworklist(apikey, org_id)
networks_table = PrettyTable()
networks_table.field_names = ["ID", "Network Name"]
for network in network_list:
    networks_table.add_row([network["id"], network["name"]])
print(networks_table)

# get network ID
network_id = input(
    f'Enter the Network ID containing the MX to add the firewalls to: ')

f = open("rules.txt", "r")
if f.mode == "r":
    f1 = f.readlines()
    rules_list = []
    for rule_line in f1:
        rules_list.append({
            'policy': 'deny',
            'protocol': 'any',
            'destPort': 'any',
            'destCidr': str.strip(rule_line)+'/32',
            'srcPort': 'any',
            'srcCidr': 'any',
            'syslogEnabled': False
        })
    meraki.updatemxl3fwrules(
        apikey, network_id, rules_list)

# fwrules = [{'comment': 'A note about the rule', 'policy': 'deny',
# 'protocol': 'tcp', 'destPort': '80,443', 'destCidr':
# '192.168.1.0/24,192.168.2.0/24', 'srcPort': 'any', 'srcCidr':
# 'any', 'syslogEnabled': True}]
