#This is made not purely by my own, I searched for much creativity of the project
#PSEUDOCODE
#START
# 1. Display the title using pyfiglet library
# 2. Display the Main menu
#   - pick option between:
#       "1. Create a quiz"
#       "2. Exit"
# 3. If the user selects "Create a quiz"
#   - Prompt the user to enter what difficulty (Elementary(as easy), High School(as medium), General(as hard))
#   - After selection, it will be in a loop for the user to input questions, choices and answers
# 4. In question loop:
#   - Ask the user to input questions
#   - If the user enter "exit" then will be redirected to main menu
#   - Otherwise, the user will be asked to input answers in the choices between a, b, c, d
#   - Prompt the user to enter the correct answer (must be in a, b, c, d)
#   - If the correct answer input is invalid, re-prompt until valid answer is given
#   - Stores the question, choices, correct answer, and difficulties in a dictionary
# 5. Write the question data to a text file in a structured format:
#   - Write the question text
#   - Write the difficulty
#   - Write the options/choices each a, b, c, d
#   - Write the correct answer
#   - Write a separator line to divide questions in text file
# 6. After saving the question, notify the user and repeat the loop to add more questions
# 7. If the user selects 'Exit' in the main menu
#   - Display goodbye message
#END

import pyfiglet

#make a function for the title
def the_title():
    title = pyfiglet.figlet_format("Welcome to the Quiz Maker!", font = 'slant')
    print (title)

#Make main menu of the code
def main_menu():
    while True:
        the_title()
        print("Main Menu")
        print("1. Create a Quiz")
        print("2. Exit")
        choice = input("Choose an option! (1 or 2): ")

        if choice == '1':
            create_quiz()
        if choice == '2':
            print("Thank you for using, Goodbye!")
            break
        else:
            print("Invalid input! Please try again ^_^")

def write_a_file(data, filename = 'quiz_questions_and_answers'):
    with open(filename, 'a',encoding = 'utf-8') as file:
        file.write("Q: " + data['question'] + "\n")
        file.write("Difficulty: " +data['difficulty'] + "\n")
        file.write("a). " + data['a'] + "\n")
        file.write("b). " + data['b'] + "\n")
        file.write("c). " + data['c'] + "\n")
        file.write("d). " + data['d'] + "\n")
        file.write("Answer: " + data['correct'] + "\n")
        file.write("-" * 40 +"\n")

def create_quiz():
    difficulty = input("Enter the difficulty (Elementary, High School, General): ").capitalize()
    print(f"Creating {difficulty} quiz. Type 'exit' as question to be redirected at main menu: ")

    while True:
        question = input("Enter your desired question (or type exit to go back to main menu)")
        if question.lower == 'exit':
            print("Returning to Main Menu...\n")
        break

    a = input("Choice a: ")
    b = input("Choice b: ")
    c = input("Choice c: ")
    d = input("Choice d: ")

    correct = ""
    while correct.lower() not in ['a', 'b', 'c', 'd']:
        correct = input("Enter the correct answer between a/b/c/d: ").lower()
        if correct not in ['a', 'b', 'c', 'd']:
            print("Invalid input! Please choose in a, b, c, d, ^_^")

    question_data =  {
        "question": question,
        "difficulty": difficulty,
        "a": a,
        "b": b,
        "c": c,
        "d": d,
        "correct": correct
    }

#Calls the function which is expected to write the quiz into a file
    write_a_file(question_data)
    print("Question is saved!!")

if __name__ == "__main__":
    main_menu()