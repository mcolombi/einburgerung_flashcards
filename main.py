import tkinter as tk
from tkinter import messagebox
import random
import json
import os

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flashcard Quiz")

        self.question_label = tk.Label(master, text="", wraplength=400, font=('Arial', 14))
        self.question_label.pack(pady=20)

        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", command=lambda idx=i: self.check_answer(idx), width=50, wraplength=250, height=3, justify='center')
            button.pack(pady=5)
            self.answer_buttons.append(button)

        self.score = 0
        self.current_question = None

        # Load questions data
        with open("data/questions.json", "r") as file:
            self.data = json.load(file)['questions']

        # Load or initialize history data
        self.history_file = "data/history.json"
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as file:
                self.history = json.load(file)
        else:
            self.history = {q['question']: {'correct': 0, 'incorrect': 0} for q in self.data}
            self.save_history()

        self.next_question()

    def save_history(self):
        with open(self.history_file, "w") as file:
            json.dump(self.history, file, indent=4)

    def next_question(self):

        # Calculate weights for each question based on history
        weights = []
        for question in self.data:
            question_text = question['question']
            correct_count = self.history[question_text]['correct']
            incorrect_count = self.history[question_text]['incorrect']
            
            # Assign weight based on incorrect count and penalize correct answers
            # Every time you answer correctly you half the probability t
            weights.append(2**(incorrect_count - correct_count))  

        # Select a question based on calculated weights
        self.current_question = random.choices(self.data, weights=weights, k=1)[0]

        self.question_label.config(text=self.current_question['question'])
        answers = self.current_question['answers']
        random.shuffle(answers)

        for i, button in enumerate(self.answer_buttons):
            button.config(text=answers[i])

            for i, button in enumerate(self.answer_buttons):
                button.config(text=answers[i])

    def check_answer(self, idx):
        selected_answer = self.answer_buttons[idx].cget("text")
        if selected_answer == self.current_question['correct_answer']:
            self.score += 1
            self.history[self.current_question['question']]['correct'] += 1
            messagebox.showinfo("Correct!", "Well done!")
        else:
            self.history[self.current_question['question']]['incorrect'] += 1
            messagebox.showerror("Incorrect!", f"The correct answer was: {self.current_question['correct_answer']}")

        self.save_history()
        self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()