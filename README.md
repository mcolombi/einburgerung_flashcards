# Grundkenntnistest flashcards - Canton Zurich

This small application creates flashcards using all the official questions of the [naturalization test of the canton Zurich](https://www.zh.ch/de/migration-integration/einbuergerung/grundkenntnistest.html).

The only dependency that is a little tricky to handle is `tkinter` as it creates some issues in vierual environments. I followed the instructions [here](https://dev.to/xshapira/using-tkinter-with-pyenv-a-simple-two-step-guide-hh5)

Running `main.py` creates flashcards of the form

<img width="488" alt="image" src="https://github.com/user-attachments/assets/5e9cec9a-65b9-4c74-8990-614cb17892c6">

A history of correct / wrong answers is kept in `history.json` and the probabilty of seeing a question increases every time it is answered incorrectly and decereases every time it was answered correctly.

In order to clear the history simply delete `hstory.json` and a new one will be created in the next run.

You can control how often you see questions you got wrong by changing the parameter `WRONG_ANSWER_PROBABILITY_MULTIPLIER` in `constants.py`. Every time you get an answer wrong the probability of selecting that question (comparatively to other questions) is multiplied by this factor. If you get the question right it is divided by this factor.


