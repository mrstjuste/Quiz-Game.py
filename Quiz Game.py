#Welcome to my quiz game!
#The file format has to be like this 
#What does CPU stand for?|a) Central Process Unit|b) Computer Personal Unit|c) Central Processing Unit*|d) Central Processor United
#What is the capital of France?|a) Madrid|b) Berlin|c) Paris*|d) Lisbon\
#Question text|a) Option a|b) Option b|c) Option c*|d) Option d
#enjoy!

import os

print("Current Working Directory:", os.getcwd())


def load_questions(filename):
    # Load questions from a file, parsing each line into question text, options, and the correct answer.
    questions = []
    #change to the file name you want here.
    with open('/Users/mrs.stjuste/Python/Github_Projects/questions.txt', 'r') as file:

        for line in file:
            parts = line.strip().split('|')
            question_text = parts[0]
            options = parts[1:5]
            answer = chr(97 + parts.index(next(filter(lambda option: option.endswith('*'), parts))))
            questions.append((question_text, options, answer))
    return questions

def display_question(question):
    # Display a question, options, and get user's answer. Return True if correct, False otherwise.
    question_text, options, answer = question
    print(question_text)
    for i, option in enumerate(options):
        print(f"{chr(97+i)}) {option.rstrip('*')}")
    return input("Your answer (a-d): ").lower() == answer

def quiz():
    # Main function to run the quiz.
    print("Welcome to my computer Quiz!")
    if input("Do you want to play? (yes/no): ").lower() != "yes":
        print("Maybe next time!")
        return
    
    questions = load_questions("questions.txt")
    score = 0
    
    for question in questions:
        if display_question(question):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    
    print(f"Quiz finished! You scored {score} out of {len(questions)}.")

quiz()
