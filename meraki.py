import requests
import json
from prettytable import PrettyTable

api_key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
headers = {'X-Cisco-Meraki-API-Key': api_key}
url = "https://api.meraki.com/api/v1"

print("ID de las organizaciones: ")
url_org = url + '/organizations'
respOrg = requests.get(url_org, headers=headers, verify=True)
jsonOrg = respOrg.json()
#print(json.dumps(jsonOrg, indent=4))

tableID = PrettyTable(["ID", "Organizaciones"])
for Organiz in jsonOrg:
    tableID.add_row([Organiz["id"], Organiz["name"]])

print(tableID)
print('-' * 100)

print("Redes de la organizacion con ID: ")
organizationId = jsonOrg[0]['id']
url_redes = url_org + '/{}/networks'.format(organizationId)
respNetwork = requests.get(url_redes, headers=headers, verify=True)
jsonNetwork = respNetwork.json()

#print(json.dumps(jsonNetwork, indent=4))
tableRedes = PrettyTable(["ID", "Redes"])
for redes in jsonNetwork:
    tableRedes.add_row([redes["id"], redes["name"]])

print(tableRedes)
print('-' * 100)

print("Dispositivos de la red con ID: ")
networkId = jsonNetwork[1]['id']
url_devices = url_redes + '/{}/devices'.format(networkId)
respDevice = requests.get(url_devices, headers=headers, verify=True)
jsonDevice = respDevice.json()
#print(json.dumps(jsonDevice, indent=4))

tableDisp = PrettyTable(["Direccion", "Serial"])
for Dispositivos in jsonDevice:
    tableDisp.add_row([Dispositivos["address"], Dispositivos["serial"]])

print(tableDisp)
print('-' * 100)

print("Datos de la  red con el networkid: ")
url_NetworkID = url + '/networks/{}'.format(networkId)
respNetworkID = requests.get(url_NetworkID, headers=headers, verify=True)
jsonNetworkID = respNetworkID.json()
#print(json.dumps(jsonNetworkID, indent=4))

Redes1 = jsonNetworkID["name"]
Redes2 = jsonNetworkID["timeZone"]

tableDatosRed = PrettyTable(["Nombre", "Zona Horaria"])
tableDatosRed.add_row([Redes1, Redes2])

print(tableDatosRed)
print('-' * 100)

print("Infomación de un dispositivo con el serial ID: ")
serial = jsonDevice[3]['serial']
url_DeviceID = url + '/networks/{}/devices/{}'.format(networkId, serial)
respDeviceID = requests.get(url_DeviceID, headers=headers, verify=True)
jsonDeviceID = respDeviceID.json()
#print(json.dumps(jsonDeviceID, indent=4))

tableNetSerie = PrettyTable(["Mac", "Modelo"])
Serie1 = jsonDeviceID["mac"]
Serie2 = jsonDeviceID["model"]
tableNetSerie.add_row([Serie1, Serie2])
print(tableNetSerie)
print('-' * 100)

print("Información del SSID para el network ID: ")
url_SSID = url + '/networks/{}/wireless/ssids'.format(networkId)
repSSID = requests.get(url_SSID, headers=headers, verify=True)
jsonSSID = repSSID.json()
#print(json.dumps(jsonSSID, indent=4))

Ssid = jsonSSID
tableWlan = PrettyTable(["Nombre", "Bandwith ", "Visible"])
for Wlan in Ssid:
    tableWlan.add_row([Wlan["name"], Wlan["bandSelection"], Wlan["visible"]])

print(tableWlan)
print('-' * 100)
