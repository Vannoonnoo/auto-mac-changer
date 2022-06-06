import winreg
import random
import os

mac         = ["28CFDA", "28E7CF", "182032", "1CABA7", "18EF63", "18DBF2", "183F47", "0C8BFD", "0C413E", "08B258"]

mac_start   = random.choice(mac)
mac_end     = random.randint(0, 2**24)

names       = ["Shawn's", "Alex's", "Jon's", "George's", "Alfred's", "Jim's", "Bob's", "Timothy's", "Fiona's", "Samantha's", "Victoria's", "Dora's", "Amy's", "Christina's"]
devices     = ["iPhone", "ThinkPad", "Dell", "Switch", "Router", "Camera", "Remote", "TV", "Modem", "Clock", "Toaster", "Toilet", "Vape Pen", "Pacemaker", "Insulin Pump", "Pain"]

pc_name     = f"{random.choice(names)} {random.choice(devices)}"

reg         = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
access_key  = winreg.OpenKey(reg, r"SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\0001", 0, winreg.KEY_SET_VALUE)

winreg.SetValueEx(access_key, "NetworkAddress", 1, winreg.REG_SZ, "%s%06X" % (mac_start, mac_end))

access_key  = winreg.OpenKey(reg, r"SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName", 0, winreg.KEY_SET_VALUE)

winreg.SetValueEx(access_key, "ComputerName", 1, winreg.REG_SZ, pc_name)

access_key  = winreg.OpenKey(reg, r"SYSTEM\CurrentControlSet\Control\ComputerName\ActiveComputerName", 0, winreg.KEY_SET_VALUE)

winreg.SetValueEx(access_key, "ComputerName", 1, winreg.REG_SZ, pc_name)

winreg.CloseKey(access_key)

os.system("netsh interface set interface Wi-Fi disable")
os.system("netsh interface set interface Wi-Fi enable")
