
# pip install noipy
# pip install requests --break-system-packages
import requests
import base64
import os

string_file_path_password = "/home/Eloi/token/no_ip.txt"

"""
cd /
sudo mkdir git
sudo mkdir token
cd token
sudo nano no_ip.txt

Copy your to no_ip.txt
USERNAME
PASSWORD
DDNS_HOSTNAME


Save Script to /git/no_ip/update.py


crontab -e
@reboot sudo python3 /git/no_ip/update.py
0 * * * * sudo python3 /git/no_ip/update.py

"""

string_file_path_password = "/token/no_ip.txt"

if not os.path.exists(string_file_path_password):
    #write directory
    string_directory_of_file = os.path.dirname(string_file_path_password)
    if not os.path.exists(string_directory_of_file):
        os.makedirs(string_directory_of_file)
    if not os.path.exists(string_file_path_password):
        with open(string_file_path_password, "w") as file:
            file.write("USERNAME\nPASSWORD\nDDNS_HOSTNAME\n")


string_token_file_content = ""
with open(string_file_path_password, "r") as file:
    string_token_file_content = file.read()


content_array = string_token_file_content.split("\n")



USERNAME= ""
PASSWORD = ""
DDNS_HOSTNAME= ""
if(len(content_array) >=1):
    USERNAME = content_array[0]

if (len(content_array) >=2):
    PASSWORD = content_array[1]
    
if (len(content_array) >=3):
    DDNS_HOSTNAME = content_array[2]  
    

print(f"Username: {USERNAME[:2]}***, Password: {PASSWORD[:2]}***, DDNS_HOSTNAME: {DDNS_HOSTNAME[:10]}***")




# GET /nic/update?hostname=mytest.example.com&myip=192.0.2.25 HTTP/1.1
# Host: dynupdate.no-ip.com
# Authorization: Basic base64-encoded-auth-string
# User-Agent: Company DeviceName-Model/FirmwareVersionNumber maintainer-contact@example.com
                
def update_ddns(username, password, hostname):
    url = f"https://dynupdate.no-ip.com/nic/update?hostname={hostname}"
    auth_string = f"{username}:{password}"
    auth_encoded = base64.b64encode(auth_string.encode()).decode()
    headers = {
        "Authorization": f"Basic {auth_encoded}",
        "User-Agent": "Company DeviceName-Model/FirmwareVersionNumber maintainer-contact@example.com"
    }
    response = requests.get(url, headers=headers)
    return response.text

if __name__ == "__main__":
    result = update_ddns(USERNAME, PASSWORD, DDNS_HOSTNAME)
    print(result)
    
    

                
                
