#!/bin/bash

# Load environment variables from .env file
export $(grep -v '^#' ../.env | xargs)

# Now you can use the environment variables
echo "SERVER_IP is: $SERVER_IP"

export DOLLAR='$'

mkdir -p "/etc/bind/zones/"

envsubst < ./zones/db.sianabipour.ir.template > /etc/bind/zones/db.sianabipour.ir 

cp ./named.conf /etc/bind/named.conf.sia

echo "Done!!"
echo ""
echo "now you have to add this line"
echo 'include "/etc/bind/named.conf.sia";'
echo 'in "/etc/bind/named.conf" then'
echo 'run "systemctl restart named"'