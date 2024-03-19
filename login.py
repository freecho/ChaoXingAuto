import base64
import requests
from Crypto.Cipher import AES


class Login:
    """
    登录类
    """

    def __init__(self, *args):
        """
        根据手机号+密码初始化对象
        :param args:
        """
        self.username = args[0]
        self.password = args[1]
        self.block_size = 16
        self.AES_KEY = "u2oh6Vu^HWe4_AES"
        self.login_url = "https://passport2.chaoxing.com/fanyalogin"
        self.session = requests.session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
            'Referer': r'http://passport2.chaoxing.com/login?fid=&newversion=true&refer=http%3A%2F%2Fi.chaoxing.com'
        }

    def pad(self, text):
        """
        对需要加密的明文进行填充补位
        :param text: 需要进行填充补位操作的明文
        :return: 补齐明文字符串
        """
        text_length = len(text)
        # 计算需要填充的位数
        amount_to_pad = self.block_size - (text_length % self.block_size)
        if amount_to_pad == 0:
            amount_to_pad = self.block_size
        # 获得补位所用的字符
        pad = chr(amount_to_pad).encode()
        return text + pad * amount_to_pad

    def encrypt(self, text):
        ciper = AES.new(self.AES_KEY.encode(), AES.MODE_CBC, self.AES_KEY.encode())
        return base64.b64encode(ciper.encrypt(self.pad(text.encode()))).decode()

    def get_information(self):
        self.username = self.encrypt(self.username)
        self.password = self.encrypt(self.password)

    def do_login(self):
        """
        登录，返回session对象
        :return:
        """
        data = {
            'fid': -1,
            'uname': self.username,
            'password': self.password,
            'refer': r'http%253A%252F%252Fi.chaoxing.com',
            't': True,
            'forbidotherlogin': 0
        }
        self.session.post(self.login_url, data=data)
        return self.session
