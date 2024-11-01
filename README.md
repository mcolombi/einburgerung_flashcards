# Grundkenntnistest flashcards - Canton Zurich

This small application creates flashcards using all the official questions of the [naturalization test of the canton Zurich](https://www.zh.ch/de/migration-integration/einbuergerung/grundkenntnistest.html).

The only dependency that is a little tricky to handle is `tkinter` as it creates some issues in vierual environments. I followed the instructions [here](https://dev.to/xshapira/using-tkinter-with-pyenv-a-simple-two-step-guide-hh5)

Running `main.py` creates flashcards of the form

<img width="484" alt="Screenshot 2024-11-01 at 08 53 44" src="https://github.com/user-attachments/assets/a34b56bb-d8b0-4e6a-a2ea-39acf6a9db02">

A history of correct / wrong answers is kept in a history file in the `data` folder and the probabilty of seeing a question increases every time it is answered incorrectly and decereases every time it was answered correctly.

You can control how often you see questions you got wrong by changing the parameter `WRONG_ANSWER_PROBABILITY_MULTIPLIER` in `settings.py`. Every time you get an answer wrong the probability of selecting that question (comparatively to other questions) is multiplied by this factor. If you get the question right it is divided by this factor.

You can change history file by modyfing `HISTORY_FILE` in settings.py. To clear history you simply delete the file and a new one will be created on the next run. Note that if you modify the questions you also need to delete the history file.








