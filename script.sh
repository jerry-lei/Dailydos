#!/bin/bash
while :
do
    sleep 1
    python /home/group/Dailydos/mail_parser.py
    > /var/mail/group
done
