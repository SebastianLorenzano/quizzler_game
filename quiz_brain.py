import html
class QuizBrain:

    def __init__(self, q_list):
        self.is_right = bool
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False):"

    def check_answer(self, players_decision):
        correct_answer = self.current_question.answer
        if correct_answer == players_decision:
            self.is_right = True
            self.score += 1
        else:
            self.is_right = False
        self.question_number += 1