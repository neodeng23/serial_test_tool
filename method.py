import winreg
import re
import json
import serial.tools.list_ports
import time
import os

cammand=[
    "set:2",
    "set:4",
    "set:6",
    "set:8",
    "set:10",
    "set:12",
    "set:14",
    "set:16",
    "set:18",
    "set:20"
    ]


def get_serial():   # 返回字典
    string = r'SYSTEM\CurrentControlSet\Control\COM Name Arbiter\Devices'   # 注册表路径
    handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, string, 0, (winreg.KEY_WOW64_64KEY + winreg.KEY_READ))
    com_list = []
    com_dict = {}

    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) == 0:
        return None
    else:
        for i in range(0, len(port_list)):
            com_name = port_list[i].name
            com_list.append(com_name)

    for x in com_list:
        location, _type = winreg.QueryValueEx(handle, x)
        com_dict[x] = location

    return com_dict


def communiate(PortName, cmd, BaudRate):
    cmd += '\r\n'
    ser = serial.Serial(PortName, int(BaudRate), timeout=float(0))
    ser.flush()

    trans_cmd = cmd.encode()
    ser.write(trans_cmd)

    ser.flush()
    ser.close()
    return ''


def test(PortName, cmd_num):
    cmd = cammand[cmd_num]
    try:
        communiate(PortName, cmd, 115200)
        return cmd, "Pass"
    except:
        return None
