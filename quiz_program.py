score = 0
quiz = {
    "1" : {
        "question" : "What is the capital of Ivory Coast",
        "answer" : "Yamoussoukro"
    },
    "2" : {
        "question" : "What is the capital of Russia",
        "answer" : "Moscow"
    },
    "3" : {
        "question" : "What is the capital of United Kingdom",
        "answer" : "London"
    },
    "4" : {
        "question" : "What is the capital of Germany",
        "answer" : "Berlin"
    },
    "5" : {
        "question" : "What is the capital of Spain",
        "answer" : "Madrid"
    },
    "6" : {
        "question" : "What is the capital of Ukraine",
        "answer" : "Keiv"
    },
    "7" : {
        "question" : "What is the capital of Italy",
        "answer" : "Rome"
    },
    "8" : {
        "question" : "What is the capital of France",
        "answer" : "Paris"
    },
    "9" : {
        "question" : "What is the capital of Belarus",
        "answer" : "Minsk"
    },
    "10" : {
        "question" : "What is the capital of Nigeria",
        "answer" : "Lagos"
    }
}


for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print("\nCorrect")
        score += 1
        print("Your score is : ", str(score), "\n")
    else:
        print("\nWrong")
        print("The answer is : ", value['answer'])
        print("Your score is : ", str(score), "\n")

print("You answered ", str(score), " out of ", len(quiz), " questions correctly")
print("Your percentage is ", str(int(score/len(quiz) * 100)), "%")