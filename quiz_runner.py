# Pseudocode
# 1. import the necessary library
# 2. The program start by initializing color formatting and defining constants
# 3. When the program is executed, it displays a title
# 4. The user is then prompted to pick the difficulty (Elementary, High School, General)
# 5. Basing on the user input, the program attempts to load/read the corresponding quiz questions from a file
# 6. Only the questions that match the selected difficulty are shown
# 7. if no question is found in the selected difficulty, it notifies the user and is redirected to the selection of difficulty
# 8. Once the question are loaded, it will be shuffled
# 9. The program presents each question to the user one by one, displaying the question and its four possible answers.
# 10.  The user has 15 seconds to answer each question. If the user does not respond in time, it is marked as unanswered.
# 11. After each question, the program checks the user’s answer:
# 12. If the answer is correct, it confirms and increases the score.
# 13. If the answer is incorrect or missing, it displays the correct answer.
# 14. After all questions have been asked, the program shows the final score out of the total number of questions.
# 15. The program then ends.

import random
import os
import pyfiglet
from inputimeout import inputimeout, TimeoutOccurred
from colorama import init,Fore, Style

init(autoreset=True)

filename = 'quiz_questions_and_answers'
time_limit = 15

def load_questions_by_difficulty:
    if not os.path.exists(filename):
        print(Fore.red = "QUIZ FILE NOT FOUND...")
        return []

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().strip()