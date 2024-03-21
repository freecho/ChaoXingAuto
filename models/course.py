class Course:
    """
    课程类, 存储课程名，课程id，班级id，个人id
    """

    def __init__(self, name, course_id, clazz_id, person_id):
        self.name = name
        self.course_id = course_id
        self.clazz_id = clazz_id
        self.person_id = person_id

    def __str__(self):
        return f"{self.name} 课程id: {self.course_id} 班级id: {self.clazz_id} 个人id: {self.person_id}"

