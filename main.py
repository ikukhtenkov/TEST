
import random

greetings = [
    "Приветствую тебя, {}!",
    "Рад тебя видеть, {}!",
    "{}! Как же ты мне нужен!",
    "Наконец-то ты здесь, {}!",
]

name = input("Твоё имя: ")
print(random.choice(greetings).format(name))
