from playsound import playsound
import json
# import random
# import time

# Open and read the JSON file
with open("quiz_questions.json", "r") as file:
    quiz_data = json.load(file)


def countdown_timer():
    # while t:
    #     mins, secs = divmod(t, 60)
    #     timer = "{:02d}:{:02d}".format(mins, secs)
    #     print(timer, end="\r")
    #     time.sleep(1)
    #     t -= 1

    print("Uh oh! You ran out of time!")


# NOT IMPLEMENTED YET!
def breakdown_quiz():
    # print("This is your full breakdown of the quiz:")
    # print(question["question"])
    pass


def structure_quiz(quiz_questions):
    score = 0
    # running = 1
    question_number = 0
    # t = 15

    for question in quiz_questions:
        # Random feature for questions BROKEN - repeating the same question.
        # question = random.choice(quiz_questions)
        question_number += 1
        print(f"\nQuestion: {question_number}")
        print(question["question"])

        for index, option_text in enumerate(question["options"]):
            option_letter = chr(65 + index)  # Convert index to a letter (A, B, C, D)
            print(f"{option_letter}) {option_text}")

        valid_answer = ["A", "B", "C", "D", "Q"]

        while True:
            try:
                answer = input("\nPick your answer: ").upper()

                # Invalid answer
                if answer not in valid_answer:
                    raise ValueError("\nInvalid input! Please enter A, B, C, D or Q(uit). ")

                # Correct answer
                if answer == question["answer"]:
                    print("Correct!")
                    print(question["explanation"])
                    score += 1
                    playsound("sounds/correct.mp3")
                    break

                # Quit the program - Return to Main Menu - NOT IMPLEMENTED YET
                elif answer == "Q":
                    print("Thanks for playing!")
                    # running = 0
                    quit()

                # Incorrect answer
                else:
                    print("Incorrect!")
                    print(f"The answer is {question['answer']} - {question['explanation']}")
                    score += 0
                    playsound("sounds/incorrect.mp3")
                    break

            # Catch ValueError as answer
            except ValueError as e:
                print(e)

    # Display final score
    print(f"\nYour final score is {score}/10")

    # Breakdown report - questions, user answer, real answer, explanation - NOT IMPLEMENTED YET!
    breakdown_quiz()


# General Knowledge Quiz
def general_knowledge_quiz():
    quiz_questions = quiz_data["General Knowledge"]

    structure_quiz(quiz_questions)


# Movies Quiz
def movies_quiz():
    quiz_questions = quiz_data["Movies"]

    structure_quiz(quiz_questions)


# Maths Quiz
def maths_quiz():
    quiz_questions = quiz_data["Maths"]

    structure_quiz(quiz_questions)


# Categories - General Knowledge, Maths, Movies
def select_category_menu():
    while True:
        print("Welcome to the Quiz Game!")
        print("\nPick a category you would like to be quizzed on!")
        print("1. General Knowledge")
        print("2. Movies")
        print("3. Maths")
        print("Q: Quit")
        select_category = input("Select a category: (1 - 3) or Q(uit) ").upper()

        if select_category == "1":
            general_knowledge_quiz()

        elif select_category == "2":
            movies_quiz()

        elif select_category == "3":
            maths_quiz()

        elif select_category == "Q":
            print("\nYou have decided to leave. Goodbye!")
            quit()

        else:
            print("\nPlease type a valid number!")


select_category_menu()
