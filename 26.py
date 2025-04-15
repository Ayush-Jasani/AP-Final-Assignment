# Problem 26
class Score:
    def __init__(self, subject, marks):
        self.subject = subject
        self.marks = marks
    
    def __str__(self):
        return f"{self.subject}: {self.marks}"


class Student:
    def __init__(self, name, subjects=None, marks=None):
        self.name = name
        self.scores = []
        
        if subjects and marks:
            if len(subjects) != len(marks):
                raise ValueError("Subjects and marks must have the same length")
            for i in range(len(subjects)):
                self.scores.append(Score(subjects[i], marks[i]))
    
    def average(self):
        if not self.scores:
            return 0
        return sum(score.marks for score in self.scores) / len(self.scores)
    
    def __str__(self):
        result = f"Student {self.name} has the following scores:"
        for score in self.scores:
            result += f"\n{score.subject}: {score.marks}"
        return result


def classAverage(students, subject):
    relevant_scores = []
    for student in students:
        for score in student.scores:
            if score.subject == subject:
                relevant_scores.append(score.marks)
    
    if not relevant_scores:
        return 0
    
    return f"{subject}:{int(sum(relevant_scores) / len(relevant_scores))}"