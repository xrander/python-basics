import random

def get_answer(answer_number):
    if answer_number == 1:
        return "it is certain"
    elif answer_number == 2:
        return "it is decidely so"
    elif answer_number == 3:
        return "Yes"
    elif answer_number == 4:
        return "Reply hazy try again"
    elif answer_number == 5:
        return "Ask again later"
    elif answer_number == 6:
        return "Concentrate and ask again"

r = random.randint(1, 6)
fortune = get_answer(r)
print(fortune)
