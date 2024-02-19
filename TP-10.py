import random

def storyGen():
    characters = ["o herói", "a princesa", "o mago", "a vilã"]
    actions = ["salvou", "derrotou", "enfeitiçou", "capturou"]
    areas = ["no castelo", "na floresta das fadas", "no reino dos mortos", "nas terras baldias"]

    character1 = random.choice(characters)
    character2 = random.choice(characters)
    action = random.choice(actions)
    area = random.choice(areas)

    story = f"{character1} {action} {character2} {area}"

    print(story)

storyGen()