print("Welcome to History Quiz Game!")


questions = ("How many years queen Elizabeth II ruled?:", "In which year was the Union Jack adopted?:",
             "Who served the longest term as prime minister?:", "How many London boroughs are there?:", "What was the Capital of England Before London?:")


options = (("A. 60 years", "B. 55 years", "C. 70 years ", "D. 68 years", "F. 72 years"),
           ("A. 1801", "B. 1918", "C. 1881", "D. 1856", "F. 1945"),
           ("A. Liz Truss", "B. Robert Walpole", "C. Margaret Thatcher",
            "D. Winston Churchill ", "F. Harold Wilson"),
           ("A. 32", "B. 28", "C. 30", "D. 33", "F. 25"),
           ("A. Margate", "B. Brighton", "C. Oxford", "D. Cardiff", "F. Winchester"))

answers = ("C", "A", "B", "A", "F")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("             ")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Well Done!")
    else:
        print("Nope!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("                      ")
print("       RESULTS        ")
print("                      ")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
