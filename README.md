# No-Ip Update From Pi Python
Just a small script to run on Pi to update the DDNS of your home to NoIP host.


https://my.noip.com/dynamic-dns  
[![image](https://github.com/user-attachments/assets/6bbfbd4c-88ac-4b41-baca-7bdd81eff521)](https://my.noip.com/dynamic-dns)  


**Note:** I hesitated to use Cloudflare because of this video:  
https://youtu.be/rI-XxnyWFnM?t=6  
However, no IP service is more dedicated to the original problem, and I have already purchased it. Maybe Cloudflare would be a better solution for you.

```
sudo nano /etc/systemd/system/no_ip_update.service
[Unit]
Description=Run No-IP update script at startup and every hour
After=network.target

[Service]
Type=oneshot
ExecStart=/usr/bin/sudo python3 /git/no_ip/update.py

[Install]
WantedBy=multi-user.target




sudo nano /etc/systemd/system/no_ip_update.timer
[Unit]
Description=Run No-IP update script every hour

[Timer]
OnBootSec=0min
OnUnitActiveSec=1h

[Install]
WantedBy=timers.target

sudo systemctl daemon-reload
sudo systemctl enable no_ip_update.service
sudo systemctl start no_ip_update.service
sudo systemctl enable no_ip_update.timer
sudo systemctl start no_ip_update.timer
systemctl list-timers | grep no_ip_update

```



# Raspberry Pi 5

[![image](https://github.com/user-attachments/assets/b4ba6702-5a73-4f0b-9cbf-baa189d7443c)](https://www.raspberrypi.com/products/raspberry-pi-5/)  
[![image](https://github.com/user-attachments/assets/0d03371a-7b4a-4013-8b58-c712f84558d2)](https://amzn.to/3VX4qL5)  
https://www.raspberrypi.com/products/raspberry-pi-5/  
Amazon: https://amzn.to/3VX4qL5  
