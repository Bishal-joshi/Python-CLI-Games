import random
print("Welcome to the KBC Game")
gamestart=input("Do you want to start the game? y/n")

questions = [
    "Which planet is known as the 'Red Planet'?",
    "Who wrote the play 'Romeo and Juliet'?",
    "In what year did World War I begin?",
    "What is the capital city of Australia?",
    "Who painted the Mona Lisa?",
    "Which element has the chemical symbol 'O'?",
    "What is the largest ocean on Earth?",
    "Who is the author of the Harry Potter book series?",
    "Which country is known as the 'Land of the Rising Sun'?",
    "What is the currency of Brazil?",
    "Who was the first woman to win a Nobel Prize?",
    "In what year did the United States declare its independence?",
    "What is the main ingredient in guacamole?",
    "Which mountain is the tallest in the world?",
    "What is the currency of Japan?",
    "Who is known as the 'Father of Computers'?",
    "What is the largest mammal in the world?",
    "In which year did the Titanic sink?",
    "What is the capital of South Africa?",
    "Who wrote the famous play 'Hamlet'?"
]

answers = [
    "Mars",
    "William Shakespeare",
    "1914",
    "Canberra",
    "Leonardo da Vinci",
    "Oxygen",
    "Pacific Ocean",
    "J.K. Rowling",
    "Japan",
    "Brazilian Real",
    "Marie Curie",
    "1776",
    "Avocado",
    "Mount Everest",
    "Japanese Yen",
    "Charles Babbage",
    "Blue Whale",
    "1912",
    "Pretoria",
    "William Shakespeare"
]


def playgame():
    random_number=random.randint(0,19)
    print(questions[random_number])
    
    options=[answers[random.randint(0,19)] for _ in range(3)]
    options.append(answers[random_number])
    random.shuffle(options)
    # print(options)
    for index,option in enumerate(options):
        print(f"{index+1} {option}")

    
    answer=input()
    
    pass
# if no then exit the game
if gamestart.lower() == "y" :
    playgame()
    print("ok here is your score")
else:
    print("thank you........")

input("press any key to exit........")
    