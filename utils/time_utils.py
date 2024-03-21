import time


def now():
    """
    获取当前时间戳，适配学习通的js时间格式（ms）
    :return:
    """
    return int(time.time() * 1000)
