import subprocess
import json
import sys
import time

# ASCII logo
logo = '''
  ____       _      _____       _   
 / ___|  ___| |_   | ____|_   _(_)  
 \___ \ / _ \ __|  |  _| \ \ / / |  
  ___) |  __/ |_   | |___ \ V /| |  
 |____/ \___|\__|  |_____| \_/ |_|  
'''

def check_wifi_status():
    try:
        wifi_info = subprocess.check_output(['termux-wifi-connectioninfo']).decode('utf-8')
        wifi_info_json = json.loads(wifi_info)
        wifi_state = wifi_info_json.get('state', 'UNKNOWN')
        return wifi_state == 'CONNECTED'
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        return False

def scan_available_wifi():
    try:
        wifi_info = subprocess.check_output(['termux-wifi-scaninfo']).decode('utf-8')
        wifi_info_json = json.loads(wifi_info)
        wifi_networks = wifi_info_json.get('scan_results', [])
        print("\n*AVAILABLE WIFI*")
        for network in wifi_networks:
            ssid = network.get('ssid', 'Unknown SSID')
            bssid = network.get('bssid', 'Unknown BSSID')
            print("SSID: {}, BSSID: {}".format(ssid, bssid))
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve WiFi network information.")

def loading_animation():
    while True:
        sys.stdout.write('\rScanning... |')
        time.sleep(0.1)
        sys.stdout.write('\rScanning... /')
        time.sleep(0.1)
        sys.stdout.write('\rScanning... -')
        time.sleep(0.1)
        sys.stdout.write('\rScanning... \\')
        time.sleep(0.1)

if __name__ == "__main__":
    print(logo)
    wifi_status = check_wifi_status()
    if not wifi_status:
        print("Turn On Your Device Wifi")
    else:
        loading_animation_thread = threading.Thread(target=loading_animation)
        loading_animation_thread.start()
        scan_available_wifi()
