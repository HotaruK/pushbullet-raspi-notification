# pushbullet-raspi-notification

## TL;DR

Use Pushbullet to monitor notifications on your Android smartphone. When you receive notifications, it will flash a full-color LED connected to Raspberry Pi.

## Setup 

### on Pushbullet

- Download Pushbullet app on your device + create your Pushbullet account
- Please read this article to learn how to get Pushbullet's API key and how to test  
    - https://medium.com/@hotakoma/receive-real-time-notifications-with-pushbullet-websockets-2bd2dc073b28


### on Raspberry Pi

- `pip install -r requirements.txt`
- Connect a full-color LED to Raspberry Pi. This program is designed to work with **RGB + anode** LED. If you use **cathode** LED, invert color outputs of Class `Color` in `LedGpioController.py`.

## Start on Raspberry Pi

`sh start.sh`
