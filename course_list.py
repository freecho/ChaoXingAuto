from bs4 import BeautifulSoup


class CourseList:
    """
    获取课程列表, 传入session，调用get_courses方法获取课程列表
    """
    def __init__(self, session):
        self.course_url = "https://mooc1-1.chaoxing.com/mooc-ans/visit/courselistdata"
        self.courses = []
        self.session = session
        self.data = {
            "courseType": 1,
            "courseFolderId": 0,
            "baseEducation": 0,
            "courseFolderSize": 0,
            "superstarClass": ""
        }

    def get_courses(self):
        """
        获取课程列表
        :return:
        """

        course_page_html = self.session.post(self.course_url, data=self.data)
        course_page = BeautifulSoup(course_page_html.text, 'html.parser')
        course_list = course_page.find_all('li', class_='course clearfix')

        for course in course_list:
            if course.find('a', class_='not-open-tip') is not None:
                continue
            course_name = course.find('span', class_='course-name overHidden2').text
            course_id = course.get("courseid")
            course_info = {
                "course_name": course_name,
                "course_id": course_id
            }
            self.courses.append(course_info)

        return self.courses
