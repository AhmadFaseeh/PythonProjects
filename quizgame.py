questions = {
    "What is the capital of Pakistan": "Islamabad",
    "What is the National Bird of Pakistan": "Falcon",
    "What is the National Animal of Pakistan": "Markhor",
    "How many provinces are there in Pakistan": "4",
}
Options = [
    ["Islambad", "Delhi", "Multan", "Biejing"],
    ["Pigeon", "Crow", "humming bird", "Falcon"],
    ["Elephant", "Lion", "Markhor", "Liger"],
    ["9", "4", "31", "23"],
]
# print(len(questions))
l = len(questions)
i = 0
for key, value in questions.items():
    # print(key)
    # print(value)
    ans = input(f"{key}?{Options[i]}: ")
    i = i + 1
    if value == ans:
        continue
    else:
        print("You are out")
        break