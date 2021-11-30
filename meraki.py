import requests
import json

api_key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
headers = {'X-Cisco-Meraki-API-Key':api_key}
url = "https://api.meraki.com/api/v1" 

print("ID de las organizaciones: ")
url_org = url +'/organizations'
respOrg = requests.get(url_org, headers=headers, verify=True)
jsonOrg = respOrg.json()
print(json.dumps(jsonOrg, indent=4))
print('-' * 100)

print("Redes de la organizacion con ID: ")
organizationId  = jsonOrg[0]['id']
url_redes = url_org + '/{}/networks'.format(organizationId)
respNetwork = requests.get(url_redes, headers=headers, verify=True)
jsonNetwork = respNetwork.json()
print(json.dumps(jsonNetwork, indent=4))
print('-' * 100)

print("Dispositivos de la red con ID: ")
networkId = jsonNetwork[1]['id']
url_devices = url_redes + '/{}/devices'.format(networkId)
respDevice = requests.get(url_devices, headers=headers, verify=True)
jsonDevice = respDevice.json()
print(json.dumps(jsonDevice, indent=4))
print('-' * 100)

print("Datos de la  red con el networkid: ")
url_NetworkID = url + '/networks/{}'.format(networkId)
respNetworkID = requests.get(url_NetworkID, headers=headers, verify=True)
jsonNetworkID = respNetworkID.json()
print(json.dumps(jsonNetworkID, indent=4))
print('-' * 100)

print("Infomación de un dispositivo con el serial ID: ")
serial =jsonDevice[3]['serial']
url_DeviceID = url + '/networks/{}/devices/{}'.format(networkId, serial)
respDeviceID = requests.get(url_DeviceID, headers=headers, verify=True)
jsonDeviceID = respDeviceID.json()
print(json.dumps(jsonDeviceID, indent=4))
print('-' * 100)

print("Información del SSID para el network ID: ")
url_SSID = url + '/networks/{}/wireless/ssids'.format(networkId)
repSSID = requests.get(url_SSID, headers=headers, verify=True)
jsonSSID = repSSID.json()
print(json.dumps(jsonSSID, indent=4))
print('-' * 100)