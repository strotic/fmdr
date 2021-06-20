#!/usr/bin/env python
import argparse
import subprocess
parser = argparse.ArgumentParser(prog="fmdr")
parser.add_argument('--usb', help='Shows USB connected drivers eg - fmdr --usb show')
parser.add_argument('--pci', help='Shows PCI connected drivers eg - fmdr --pci show')
args = parser.parse_args()

if args.usb:
    print("FMDR found the following")
    print(" -.-.-.-.-.-.-.-.-.-.-.")

    print(subprocess.call(["lsusb"]))

    print(".-.-.-.--.-.-.-.-.-.-.-.-")

elif args.pci:
    print("FMDR found the following")
    print(".-.-.-.--.-.-.-.-.-.-.-.-")


    print(subprocess.call(["lspci"]))

    print(".-.-.-.--.-.-.-.-.-.-.-.-.-.-.-.--.-.-.-.-.-.-.-.-")
    print("github.com/strotic")
    print("Any bugs please open a Issues tab.")

else:
    print("Please use the correct syntax")

#getinfo = subprocess.call(["lsusb"])
#print(getinfo)
