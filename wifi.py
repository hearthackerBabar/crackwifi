import subprocess
import json
import sys
import time
import threading
import os

# Clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ANSI color codes
GREEN = '\033[92m'  # Green color
RESET = '\033[0m'    # Reset color

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
    except (FileNotFoundError, subprocess.CalledProcessError, json.JSONDecodeError):
        return False

def scan_available_wifi():
    try:
        # Increase timeout for retrieving WiFi scan information
        wifi_info = subprocess.check_output(['termux-wifi-scaninfo', '-t', '10']).decode('utf-8')
        wifi_info_json = json.loads(wifi_info)
        wifi_networks = wifi_info_json.get('scan_results', [])
        print("\n*AVAILABLE WIFI*")
        for i, network in enumerate(wifi_networks[:5], start=1):  # Limit to first 5 networks
            ssid = network.get('ssid', 'Unknown SSID')
            bssid = network.get('bssid', 'Unknown BSSID')
            # Display in green color
            print(f"{i}. SSID: {GREEN}{ssid}{RESET}, BSSID: {GREEN}{bssid}{RESET}")
            # Reduce delay between each network print statement
            time.sleep(0.1)
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        print("Error: Unable to retrieve WiFi network information.")

def loading_animation():
    while True:
        sys.stdout.write('\rScanning...')
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\r           ')
        sys.stdout.flush()
        time.sleep(0.5)

def scan_wifi():
    wifi_status = check_wifi_status()
    if not wifi_status:
        print("Turn On Your Device Wifi")
        return

    # Clear the screen and display the logo
    clear_screen()
    print(logo)
    
    # Display "Scanning WiFi networks..." in green color
    print(f"{GREEN}Scanning WiFi networks...{RESET}")

    loading_thread = threading.Thread(target=loading_animation)
    loading_thread.start()
    scan_available_wifi()
    loading_thread.join()  # Wait for the loading animation to finish

if __name__ == "__main__":
    clear_screen()
    print(logo)
    print("1. Scan WiFi")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        scan_wifi()
    elif choice == '2':
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice. Please enter either 1 or 2.")
