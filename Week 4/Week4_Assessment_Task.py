import json
R1 = '''{
    "hostname": "R1",
    "enable": "cisco",
    "motd": "Unauthorised access is prohibited",
    "encryption": "True",
    "ip_address": "192.168.100.10",
    "username": "cisco",
    "password": "cisco123!"
}'''
dictionary = json.loads(R1)
dictionary.pop("motd", None)
print(dictionary)
print("Key\tValue")
for key, value in dictionary.items():
    print(f"{key}\t{value}")
