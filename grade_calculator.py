from re import sub

""" SPECIFIC TO CS220 FALL 2022"""
""" 
        TO BE DONE 
 1. Missing grade
 2. Final desired score
 3. Grade Prediction
 4. Future grades influence
 5. Grade proportion 

"""

class GradeCalculator:

    categories = {
        "Quiz" : .3,
        "Project" : .35,
        "Term Project" : 0.1,
        "Warm Up" : 0,
        "Final" : 0.25
    }

    categories_without_final = {
        "Quiz" : .4,
        "Project" : .4667,
        "Term Project" : 0.1334
    }

    def __init__(self):
        self.grades = {}
        self.final = 0
        self.sub_scores = {
            "Quiz" : 0,
            "Project" : 0,
            "Term Project" : 0,
            "Warm Up" : 0,
            "Final" : 0
        }


    def __init__(self, grades: dict):
        self.grades = grades        
        self.final = 0
        self.sub_scores = {
            "Quiz" : 0,
            "Project" : 0,
            "Term Project" : 0,
            "Warm Up" : 0,
            "Final" : 0
        }

    """ ______TEMPORARY FOR REFERENCE_______"""
    def quiz_average(grades: dict) -> float:
        def get_score(score: str) -> float:
            got = float(score.split("/")[0])
            out = float(score.split("/")[1])
            return (got / out * 100)
        def average_score(scores: list) -> float:
            all = sum(scores)
            return all / len(scores)
        scores = []
        for ass, score in grades.items():
            if "Quiz" in ass:
                scores.append(get_score(score))
        print(scores)
        
        return average_score(scores)
        

    def get_subscore(self, grades: dict, category: str) -> float:

        def get_score(score: str) -> float:
            got = float(score.split("/")[0])
            out = float(score.split("/")[1])
            return (got / out * 100)

        def average_score(scores: list) -> float:
            all = sum(scores)
            return all / len(scores)
            
        scores = []
        # handle "Project" and "Term Project"
        if category == "Term Project":
            category = "Term"

        for ass, score in grades.items():
            if category in ass:
                scores.append(get_score(score))
        subscore = 0
        if len(scores) != 0:
            subscore = average_score(scores)
        return subscore

    def calculate_subscores(self):
        
        for category in self.categories:
            self.sub_scores[category] = self.get_subscore(self.grades, category)

    def print_quiz_scores(self):
        for i in self.grades:
            if "Quiz" in i:
                print(self.grades[i])

    #def grades_information(self):


    def grade_for_class(self):
        # without taking into account FINAL
        score = 0
        for cat in self.categories_without_final:
            score += self.sub_scores[cat] * self.categories_without_final[cat]
        return score