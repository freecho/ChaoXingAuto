import requests
import utils.time_utils as time_utils

from models.course import Course
from models.active import Active


class ActiveList:
    """
    获取课程的活动列表，捕获签到活动
    """

    def __init__(self, session: requests.Session, course: Course):
        self.active_list = []
        self.session = session
        self.active_url = f"http://mobilelearn.chaoxing.com/v2/apis/active/student/activelist?fid=0" \
                          f"&courseId={course.course_id}" \
                          f"&classId={course.clazz_id}&showNotStartedActive=0&_={time_utils.now()}"

    def get_check_in_list(self):
        """
        返回有效的签到活动列表
        :return:
        """
        response_json = self.session.get(self.active_url).json()
        response = response_json.get("data").get("activeList")
        for active in response:
            # 获取有效的签到活动
            if active.get("activeType") == 2 and active.get("status") == 1:
                self.active_list.append(
                    Active(active.get("id"), active.get("nameOne"), active.get("activeType"), active.get("startTime"),
                           active.get("endTime"),
                           ohther_id=active.get("otherId")))

        return self.active_list
