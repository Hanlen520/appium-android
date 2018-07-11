#######################################################
# FileName:write_user_command.py
# Author:liketao
# Date:2018-7-2
# Function Description: yaml�ļ���ȡ��д�롢����ķ���
#######################################################

import yaml


class WriteUserCommand:
    def read_data(self):
        """
        ����yaml����
        :return:
        """
        with open("../Data/userconfig.yaml") as fr:
            data = yaml.load(fr)
            return data

    def get_value(self, key, port):
        """
        ��ȡvalue
        :param self:
        :param key:
        :param port:
        :return:
        """
        data = self.read_data()
        value = data[key][port]
        return value

    def write_data(self, i, device, platformversion, bp, port):
        """
        д������
        :param i:
        :param device:
        :param bp:
        :param port:
        :return:
        """
        data = self.join_data(i, device, platformversion, bp, port)
        with open("../Data/userconfig.yaml", "a") as fr:
            yaml.dump(data, fr)

    def join_data(self, i, device, platformversion, bp, port):
        data = {
            "user_info_" + str(i): {
                "deviceName": device,
                "platformVersion": platformversion,
                "bp": bp,
                "port": port,
            }
        }
        return data

    def clear_data(self):
        with open("../Data/userconfig.yaml", "w") as fr:
            fr.truncate()
        fr.close()

    def get_file_lines(self):
        data = self.read_data()
        return len(data)


if __name__ == '__main__':
    write_file = WriteUserCommand()
    print(write_file.get_file_lines())
