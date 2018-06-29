#定义全局变量
class GlobalVar:
    username = 'autotest1'
    password = '123456'
    email = 'autotest1@qq.com'

def get_username():
    return GlobalVar.username

def get_password():
    return GlobalVar.password

def get_email():
     return  GlobalVar.email