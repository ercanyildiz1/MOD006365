import json
import re
from netmiko import ConnectHandler

with open("device_details.json", "r") as json_file:
    device_details = json.load(json_file)

net_connect = ConnectHandler(**device_details)

output = net_connect.send_command("show version")

net_connect.disconnect()

hostname_pattern = re.compile(r"Hostname: (\S+)")
ios_version_pattern = re.compile(r"Cisco IOS Software, (\S+),")
processor_id_pattern = re.compile(r"Processor board ID (\S+)")
config_register_pattern = re.compile(r"Configuration register is (\S+)")

hostname = hostname_pattern.search(output).group(1)
ios_version = ios_version_pattern.search(output).group(1)
processor_id = processor_id_pattern.search(output).group(1)
config_register = config_register_pattern.search(output).group(1)

print(f"Hostname: {hostname}")
print(f"IOS Version: {ios_version}")
print(f"Processor ID: {processor_id}")
print(f"Config Register: {config_register}")