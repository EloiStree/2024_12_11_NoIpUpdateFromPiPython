# No-Ip Update From Pi Python
Just a small script to run on Pi to update the DDNS of your home to NoIP host.


https://my.noip.com/dynamic-dns  
[![image](https://github.com/user-attachments/assets/6bbfbd4c-88ac-4b41-baca-7bdd81eff521)](https://my.noip.com/dynamic-dns)  



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




sudo nano /etc/systemd/system/noip_update.timer
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
