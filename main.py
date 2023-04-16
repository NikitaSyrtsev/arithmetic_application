import random
def get_difficulty_level():
    while True:
        print(
            "Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29")
        level = input()
        if level == "1":
            # diff_level_storage()
            return get_task_one()
        elif level == "2":
            return get_task_two()
        else:
            print("Incorrect format.")

def get_task_one():
    correct_answers = 0
    for i in range(5):
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        z = random.choice("+-*")
        result = f'{str(x)} {z} {str(y)}'
        print(result)
        while True:
            answer = input()
            try:
                # try to convert the answer to an integer
                answer_int = int(answer)
                if answer_int == eval(result):
                    print("Right!")
                    correct_answers += 1
                    break
                else:
                    print("Wrong!")
                    break
            except ValueError:
                print("Wrong format! Try again.")
                print(result)
    print(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.")
    save_results(correct_answers, 1)


def get_task_two():
    correct_answers = 0
    for i in range(5):
        x = random.randint(11, 29)
        result = str(x ** 2)
        print(x)
        while True:
            answer = input()
            try:
                # try to convert the answer to an integer
                answer_int = int(answer)
                if answer_int == eval(result):
                    print("Right!")
                    correct_answers += 1
                    break
                else:
                    print("Wrong!")
                    break
            except ValueError:
                print("Wrong format! Try again.")
                print(result)
    print(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.")
    save_results(correct_answers, 2)


def save_results(correct_answers, difficulty):
    answer = input().lower()
    if answer in ["yes", "y"]:
        print("What is your name?")
        name = input()
        with open("results.txt", "a") as f:
            f.write(f"{name}: {correct_answers}/5 in level {difficulty} ")
            if difficulty == 1:
                f.write("(simple operations with numbers 2-9)\n")
            elif difficulty == 2:
                f.write("(integral squares of 11-29)\n")
        print('The results are saved in "results.txt".')
    else:
        None


get_difficulty_level()
