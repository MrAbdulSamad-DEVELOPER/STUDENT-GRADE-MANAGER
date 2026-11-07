"""Student grade manager.

Add students, record their marks, and get averages,
letter grades and class rankings.
"""


def letter_grade(average):
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


class GradeManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name in self.students:
            raise ValueError(f"Student '{name}' already exists.")
        self.students[name] = []

    def add_marks(self, name, marks):
        if name not in self.students:
            raise ValueError(f"Student '{name}' not found.")
        if not isinstance(marks, (int, float)) or isinstance(marks, bool):
            raise TypeError("Marks must be a number.")
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")
        self.students[name].append(marks)

    def average(self, name):
        if name not in self.students:
            raise ValueError(f"Student '{name}' not found.")
        marks = self.students[name]
        if not marks:
            return 0.0
        return sum(marks) / len(marks)

    def grade(self, name):
        return letter_grade(self.average(name))

    def ranking(self):
        ranked = sorted(
            self.students.keys(),
            key=lambda name: self.average(name),
            reverse=True,
        )
        return [(name, round(self.average(name), 2), self.grade(name)) for name in ranked]

    def class_average(self):
        if not self.students:
            return 0.0
        totals = [self.average(name) for name in self.students]
        return round(sum(totals) / len(totals), 2)


def main():
    gm = GradeManager()
    gm.add_student("Sara")
    gm.add_student("Ali")
    gm.add_marks("Sara", 85)
    gm.add_marks("Sara", 92)
    gm.add_marks("Ali", 78)
    gm.add_marks("Ali", 88)
    print("Class ranking:")
    for rank, (name, avg, grade) in enumerate(gm.ranking(), start=1):
        print(f"{rank}. {name}: {avg} ({grade})")
    print(f"Class average: {gm.class_average()}")


if __name__ == "__main__":
    main()
