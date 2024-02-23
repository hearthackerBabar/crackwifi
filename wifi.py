import subprocess

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
    ip_address = subprocess.check_output(['ip', 'addr', 'show', 'wlan0']).decode('utf-8').split("inet ")[1].split("/")[0]
    print("Your IP Address: ", ip_address)

# Display all WiFi networks near the device
def list_nearby_wifi():
    wifi_list = subprocess.check_output(['iwlist', 'wlan0', 'scan']).decode('utf-8').split("ESSID:")
    wifi_networks = [wifi.split("Encryption key:")[0].strip() for wifi in wifi_list if "Encryption key" in wifi]
    print("\nWiFi Networks Near You:")
    for network in wifi_networks:
        print(network)

get_ip_address()
list_nearby_wifi()