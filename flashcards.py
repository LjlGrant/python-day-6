# In Comments write out what you think the functions should be

# quit_app
# get_random_question
# show_question
# show_answer

import random

flashcards = [
    {"question": "What Python keyword is used to define a function?", "answer": "def"},
    {"question": "What Python data type represents WHOLE numbers?", "answer": "int"},
    {"question": "What data structure is used to represent Key, Value pairs?", "answer": "dictionary"}
]

'''
Task: Tell the user goodbye.
Input: None
Side Effect: Prints a goodbye message to Terminal.
Return: None
'''
def quit_app():
    print("Thanks for studying come back soon or you'll fail your test!")

'''
Task: Selects and Retrieves a Random Elements in the Flashcards list
Input: Flashcards list
Side Effect: None
Return: the Flashcards (dictionary)
'''
def get_random_question(cards):
    random_card = random.choice(cards)
    return random_card

'''
Task: Display the question.
Input: Question card.
Side Effect: Print the question text to Terminal.
Return: None
'''

def show_question(card):
    question = card["question"]
    print("Question:", question)
'''

Task: Display the answer.
Input: Question card.
Side Effect: Print the answer text to Terminal,
Return: None
'''

def show_answer(card):
    answer = card["answer"]
    print("Answer:", answer)

def main():
    while True:
        chosen_card = get_random_question(flashcards)
        show_question(chosen_card)

        user_choice = input("Enter Q to quit, type anything else to continue.")

        if user_choice == "Q":
            quit_app()
            break

        else:
            show_answer(chosen_card)


main()

    


