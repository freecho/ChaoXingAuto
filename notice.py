# {"status":true,"objs":"555EC49B0A097FBC7930AAA6FC4C4A98"}
class Notice:
    """
    收件箱
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
