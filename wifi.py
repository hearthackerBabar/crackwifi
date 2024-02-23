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
    try:
        ip_info = subprocess.check_output(['ifconfig', 'wlan0']).decode('utf-8')
        ip_address = ip_info.split("inet ")[1].split(" ")[0]
        print("Your IP Address: ", ip_address)
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve IP address.")
    except IndexError:
        print("Error: No IP address found for wlan0.")

# Display all WiFi networks near the device
def list_nearby_wifi():
    try:
        wifi_list = subprocess.check_output(['iwlist', 'wlan0', 'scan']).decode('utf-8').split("ESSID:")
        wifi_networks = [wifi.split("Encryption key:")[0].strip() for wifi in wifi_list if "Encryption key" in wifi]
        print("\nWiFi Networks Near You:")
        for network in wifi_networks:
            print(network)
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve WiFi network information.")

get_ip_address()
list_nearby_wifi()
