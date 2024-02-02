import random


def random_walk(n):
    x = 0
    y = 0
    for i in range(n):
        step = ""
        RN = random.randint(1, 10)
        if 0 < RN < 4:
            step = "UP"
        elif 3 < RN < 6:
            step = "Down"
        elif 5 < RN < 8:
            step = "RIGHT"
        elif 7 < RN < 10:
            step = "LEFT"

        if step == "UP":
            y += 1
        elif step == "DOWN":
            y -= 1
        elif step == "RIGHT":
            x += 1
        elif step == "LEFT":
            x -= 1
    return (x, y)


for i in range(10):
    print(random_walk(10))
