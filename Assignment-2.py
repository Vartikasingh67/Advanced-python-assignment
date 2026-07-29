def report_format(function):
    def wrapper(self):
        print("-" * 40)
        print("REPORT GENERATOR")
        print("-" * 40)

        function(self)

        print("-" * 40)
        print("END OF REPORT")
        print("-" * 40)

    return wrapper


class Report:

    def __init__(self, title, section):
        self.title = title
        self.section = section

    @classmethod
    def student_report(cls):
        title = "STUDENT PERFORMANCE REPORT"
        section = [
            "STUDENT NAME: RAHUL",
            "ROLL NO: 101",
            "COURSE: PYTHON",
            "GRADE: A"
        ]
        return cls(title, section)

    @report_format
    def display(self):
        print("Title:", self.title)
        print()

        for item in self.section:
            print(item)

    def __str__(self):
        return f"Report Title : {self.title}"

    def __len__(self):
        return len(self.section)


report = Report.student_report()

print(report)

print("Total Section:", len(report))

print()

report.display()
