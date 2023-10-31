from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random

class GeneralKnowledgeQuizApp(App):
    def __init__(self, **kwargs):
        super(GeneralKnowledgeQuizApp, self).__init__(**kwargs)
        self.all_questions = [
            {"question": "What is the date of the United States' Declaration of Independence?", "answer": "July 4, 1776"},
            {"question": "In which year did the French Revolution begin?", "answer": "1789"},
            {"question": "During which years did World War II take place?", "answer": "1939-1945"},
            # You can add more questions here
        ]

        self.other_questions = [
            {"question": "What is the capital of the United Kingdom?", "answer": "London"},
            {"question": "Which element has the chemical symbol Fe?", "answer": "Iron"},
            {"question": "Between which two countries did the Hundred Years' War take place?", "answer": "England and France"},
            # You can add more questions here
        ]

        self.questions = self.all_questions.copy() + self.other_questions.copy()
        random.shuffle(self.questions)

        self.score = 0
        self.level = 1
        self.questions_per_level = 3
        self.max_level = 10
        self.index = random.randint(0, len(self.questions) - 1)

    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.info_panel = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.score_label = Label(text=f"Score: {self.score}", size_hint=(0.5, 1))
        self.level_label = Label(text=f"Level: {self.level}", size_hint=(0.5, 1))
        self.info_panel.add_widget(self.score_label)
        self.info_panel.add_widget(self.level_label)
        layout.add_widget(self.info_panel)

        self.question_label = Label(text=self.questions[self.index]["question"])
        layout.add_widget(self.question_label)
        self.answer_input = TextInput(hint_text="Enter your answer")
        layout.add_widget(self.answer_input)
        self.answer_button = Button(text="Answer")
        self.answer_button.bind(on_release=self.answer)
        layout.add_widget(self.answer_button)

        self.restart_button = Button(text="Restart")
        self.restart_button.bind(on_release=self.restart)
        layout.add_widget(self.restart_button)

        return layout

    def answer(self, instance):
        answer = self.answer_input.text
        if answer.lower() == self.questions[self.index]["answer"].lower():
            self.score += 1
            self.score_label.text = f"Score: {self.score}"
            if self.score == self.questions_per_level:
                self.level += 1
                self.score = 0
                self.questions_per_level += 1
                self.level_label.text = f"Level: {self.level}"
            self.questions.pop(self.index)
            if self.questions:
                self.index = random.randint(0, len(self.questions) - 1)
                self.question_label.text = self.questions[self.index]["question"]
                self.answer_input.text = ""
            else:
                self.question_label.text = "Congratulations, you answered all questions correctly!"
                self.answer_input.text = ""
                self.answer_button.text = "Restart"
                self.answer_button.unbind(on_release=self.answer)
        else:
            self.questions = self.all_questions.copy() + self.other_questions.copy()
            random.shuffle(self.questions)
            self.index = random.randint(0, len(self.questions) - 1)
            self.question_label.text = self.questions[self.index]["question"]
            self.answer_input.text = ""
            self.score = 0
            self.level = 1
            self.score_label.text = f"Score: {self.score}"
            self.level_label.text = f"Level: {self.level}"
            self.question_label.text = "You gave a wrong answer. Start over."

        if self.level > self.max_level:
            self.question_label.text = "Congratulations, you won the game!"
            self.answer_input.text = ""
            self.answer_button.disabled = True

    def restart(self, instance):
        self.questions = self.all_questions.copy() + self.other_questions.copy()
        random.shuffle(self.questions)
        self.index = random.randint(0, len(self.questions) - 1)
        self.score = 0
        self.level = 1
        self.score_label.text = f"Score: {self.score}"
        self.level_label.text = f"Level: {self.level}"
        self.question_label.text = self.questions[self.index]["question"]
        self.answer_input.text = ""
        self.answer_button.text = "Answer"
        self.answer_button.bind(on_release=self.answer)

if __name__ == '__main__':
    GeneralKnowledgeQuizApp().run()
