class Active:
    """
    活动类 存储签到，测试等活动信息
    """

    # activeType==2 为签到，status==1 为有效的活动
    # otherId 表示签到类型：0为普通签到  5为密码签到  3为手势签到 4为位置签到 2为二维码签到
    def __init__(self, active_id, name, active_type, start_time, end_time, **kwargs):
        self.active_id = active_id
        self.name = name
        self.active_type = active_type
        self.start_time = start_time
        self.end_time = end_time

        self.__dict__.update(kwargs)

    def __repr__(self):
        return f"活动ID:{self.active_id} 活动类型:{self.active_type} 开始时间:{self.start_time} 结束时间:{self.end_time} 其他信息:{self.__dict__}"
