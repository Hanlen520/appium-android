#######################################################
# FileName:Server.py
# Author:liketao
# Date:2018-6-20
# Function Description: AppiumServer类，相关启动、多线程并行方法
#######################################################

from Mobile_Testsuite.untils.dos_cmd import DosCmd
from Mobile_Testsuite.untils.port import Port
import threading
import time


class Server(object):
    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_devices()

    def get_devices(self):
        """
        获取设备信息
        """
        devices_list = []
        result_list = self.dos.excute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list

        else:
            return None

    def create_port_list(self, start_port):
        """
        创建可用端口
        :param start_port:
        :return:
        """
        port = Port()
        port_list = []
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self, i):
        """
        生成命令
        :param i:
        :return:
        """
        #appium -p 4700 -bp 4701 -U 127.0.0.1:21503

        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        device_list = self.device_list
        command = 'appium -p' + str(appium_port_list[i]) + '-bp' + str(bootstrap_port_list[i]) + '-U' + device_list[i] + '--no-reset --session-override'
        command_list.append(command)

        return command_list

    def start_server(self, i):
        """
        启动Appium服务器
        :param i:
        :return:
        """
        self.start_list = self.create_command_list(i)
        print(self.start_list)

        self.dos.excute_cmd(self.start_list[0])

    def kill_server(self):
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list)>0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')

if __name__ == '__main__':
    server = Server()
    print(server.get_devices())
