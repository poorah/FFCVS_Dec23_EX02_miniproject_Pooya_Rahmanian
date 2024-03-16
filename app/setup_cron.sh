#!/bin/bash

# Ensure crontab exists
touch /etc/crontab
touch /var/log/cron.log

apt update
apt install -y python3
apt install -y cron

# Add cron job entry
crontab -l >/tmp/c1
echo "* * * * * root /usr/bin/python3 /codes/get_data.py" >> /tmp/c1
crontab /tmp/c1
crontab -l
# An empty line is required at the end of this file for a valid cron file.


