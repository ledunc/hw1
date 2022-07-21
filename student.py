# Task 2
class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = {}


class CFGStudent(Student):

    def __init__(self, name, age, id):
        super().__init__(name, age, id)

    def add_subject_and_grade(self, subject_n_grade):
        self.subjects.update(subject_n_grade)

    def remove_subject(self, subject):
        self.subjects.pop(subject)

    def view_all_subjects(self):
        print("-Grade Report-")
        for subject, grade in self.subjects.items():
            print(f"{subject:10} {grade}%")
        print("--------------")

    def overall_grade(self):
        average = sum(self.subjects.values())/len(self.subjects.keys())
        print(f"Overall Grade: {average:.0f}%")


# initialise myself as a CFG student
myself = CFGStudent('Lydia', 23, 1000)

# adding my topics and grades
myself.add_subject_and_grade({'Python': 90})
myself.add_subject_and_grade({'OOP': 87})
myself.add_subject_and_grade({'SQL': 92})
myself.add_subject_and_grade({'Iteration': 100})

# removing iteration as a topic as it is not correct
myself.remove_subject('Iteration')

# see all my subjects
myself.view_all_subjects()

# average of my overall grade
myself.overall_grade()