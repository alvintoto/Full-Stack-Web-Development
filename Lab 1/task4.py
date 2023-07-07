class Course:
    def __init__(self, department, number, name, credits, days, start, end, avg_grade):
        self.department = department
        self.number = number
        self.name = name
        self.credits = credits
        self.days = days
        self.start = start
        self.end = end
        self.avg_grade = avg_grade

    def format(self, index):
        return (
            f"COURSE {index}: {self.department}{self.number}: {self.name}\n"
            f"Number of Credits: {self.credits}\n"
            f"Days of Lectures: {self.days}\n"
            f"Lecture Time: {self.start} - {self.end}\n"
            f"Stat: on average, students get {self.avg_grade}% in this course\n\n"
        )

def format_classes():
    courses = []
    with open("classesInput.txt", "r") as file:
        num_courses = int(file.readline().strip())
        for i in range(num_courses):
            department = file.readline().strip()
            number = file.readline().strip()
            name = file.readline().strip()
            credits = file.readline().strip()
            days = file.readline().strip()
            start = file.readline().strip()
            end = file.readline().strip()
            avg_grade = file.readline().strip()
            courses.append(
                Course(department, number, name, credits, days, start, end, avg_grade)
            )

    with open("classesOutput.txt", "w") as file:
        for i, course in enumerate(courses):
            file.write(course.format(i + 1))

format_classes()