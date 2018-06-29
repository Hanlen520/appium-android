import os
from Mobile_Testsuite.untils.dos_cmd import DosCmd


class Port:
    def __init__(self):
        self.dos = DosCmd()

    def port_is_used(self, port_num):
        """
        判断端口是否被占用
        :param port_num:
        :return:
        """
        flag = None
        command = 'netstat -ano | findstr' + str(port_num)
        result = self.dos.excute_cmd_result(command)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, device_list):
        """
        生成可用端口
        :param start_port:
        :param device_list:
        :return:
        """
        port_list = []
        if device_list is not None:
            while len(port_list) != len(device_list):
                if not self.port_is_used(start_port):
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print('生成可用端口失效')
            return None

if __name__ == '__main__':
    port = Port()
    li = ['e59ac27c', 'JDM5T15A13000205']
    print(port.create_port_list(4722, li))