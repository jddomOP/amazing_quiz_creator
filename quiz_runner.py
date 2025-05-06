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

def load_questions_by_difficulty(difficulty):
    if not os.path.exists(filename):
        print(Fore.RED + "QUIZ FILE NOT FOUND...")
        return []

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().strip()

    question_blocks = content.split("-" * 40 + "\n")
    questions = []

    for block in question_blocks:
        lines = block.strip.split('\n')
        if len(lines) < 7:
            continue

        question_data = {
            "question": lines[0][3:],
            "difficulty": lines [1][11:].strip().lower(),
            "a": lines[2][4:],
            "b": lines[3][4:],
            "c": lines[4][4:],
            "d": lines[5][4:],
            "correct": lines[6][8:].lower()
        }

        if question_data['difficulty'] == difficulty.lower():
            question.append(question_data)

    return questions

def ask_question(questions):
    score = 0
    random.shuffle(questions)

    for i, q in enumerate(questions, 1):
        print(Fore.YELLOW + F"\n Question {i}: {q['question']}")
        print(f"a.) {q['a']}")
        print(f"b.) {q['a']}")
        print(f"c.) {q['a']}")
        print(f"d.) {q['a']}")
        print(Fore.BLUE + f"⏳ You have {time_limit} seconds to answer!!")

        try:
            answer = inputimeout(prompt=Fore.CYAN + "Your answer (a/b/c/d): ", timeout= time_limit).lower()
        except TimeoutOccurred:
            answer = None
            print(Fore.RED + "⌛ Time is up!" )

        if answer in ['a', 'b', 'c', 'd'] and answer == q['correct']:
            print(Fore.GREEN + "Correct!!")
            score += 1
        elif answer:
            print(Fore.RED + f"❌ Wrong! The correct answer was '{q['correct']} {q[q['correct']]}")
        else:
            print(Fore.RED + f"❌ No answer?!?!, The correct answer was '{q['correct']} {q[q['correct']]}")

    print(Fore.MAGENTA + f"\n Quiz Finished!! Your Score: {score}/{len(question)}")

def choose_difficulty():
    difficulty_map = {'1': 'Elementary', '2': 'High School', '3': 'General'}

    while True:
        print(Fore.CYAN + "🔍 Select difficulty:")
        print("1. Elementary")
        print("2. High School")
        print("3. General")
        choice = input(Fore.CYAN + "Enter 1/2/3: ")

        if choice not in difficulty_map:
            print(Fore.RED + "❌ Invalid choice. Please choose between 1, 2, 3")
            continue

        difficulty = difficulty_map [choice]
        questions = load_questions_by_difficulty(difficulty)

        if questions:
            return difficulty, questions
        else:
            print(Fore.RED + f"No questions found for '{difficulty}'. Please pick another difficulty. \n")

def main():
    print(Fore.LIGHTCYAN_EX + pyfiglet.figlet_format("Welcome to my Quiz!!", font="slant"))
    difficulty, question = choose_difficulty()
    ask_question(questions)

if __name__ == "__main__":
    main()

#major debugging of my code