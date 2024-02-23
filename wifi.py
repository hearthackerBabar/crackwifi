import subprocess
import json

# Display WiFi ASCII art logo
wifi_logo = '''
  _______   __          __        ______     ______     __     __   __     ______    
 /       \\ /  \\        /  |      /      \\   /      \\   /  \\   /  | /  |   /      \\   
 $$$$$$$  |$$  \\      /$$ |     /$$$$$$  | /$$$$$$  | /$$  \\ /$$ | $$ |  /$$$$$$  |  
 $$ |__$$ |$$$  \\    /$$$ |     $$ |  $$ | $$ |  $$ | $$$  |$$$ | $$ |  $$ |  $$ |  
 $$    $$/$$$$$  \\  /$$$$ |     $$ |  $$ | $$ |  $$ | $$$$ |$$$$ | $$ |  $$ |  $$ |  
 $$$$$$$/  $$ $$  \\/$$ $$ |    $$ |  $$ | $$ |  $$ | $$ $$ $$ | $$ |  $$ |  $$ |  
 $$ |      $$ \\$$ $$/  $$ |____ $$ \\__$$ | $$ \\__$$ | $$ |$$$$ | $$ | _$$ |_ $$ |  
 $$ |      $$ | \\$$$/   $$       |$$    $$/  $$    $$/  $$ | $$$ | $$ |/ $$   |$$ |  
 $$/       $$ | \\$$/    $$$$$$$$/  $$$$$$/    $$$$$$/   $$/   $$/  $$/ $$$$$$/  
             $$ |                                                            
             $$ |                                                            
             $$/                                                             
'''

print(wifi_logo)

# Display user's IP address
def get_ip_address():
    try:
        ip_info = subprocess.check_output(['termux-wifi-connectioninfo']).decode('utf-8')
        ip_info_json = json.loads(ip_info)
        ip_address = ip_info_json.get('ip', 'Unknown')
        print("Your IP Address: ", ip_address)
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve IP address.")
    except KeyError:
        print("Error: No IP address found.")

# Display all available WiFi networks
def list_available_wifi():
    try:
        wifi_info = subprocess.check_output(['termux-wifi-scaninfo']).decode('utf-8')
        wifi_info_json = json.loads(wifi_info)
        wifi_networks = wifi_info_json.get('scan_results', [])
        print("\n*AVAILABLE WIFI*")
        for network in wifi_networks:
            ssid = network.get('ssid', 'Unknown SSID')
            bssid = network.get('bssid', 'Unknown BSSID')
            print(f"SSID: {ssid}, BSSID: {bssid}")
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve WiFi network information.")

get_ip_address()
list_available_wifi()
