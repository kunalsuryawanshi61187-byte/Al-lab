m = 4  # capacity of jug1
n = 3  # capacity of jug2
goal = 2

jug1 = 0
jug2 = 0

print(f"Initial State: ({jug1}, {jug2})")

while True:
    # If goal is reached
    if jug1 == goal or jug2 == goal:
        print(f"Goal reached: ({jug1}, {jug2})")
        break

    # Rule 1: If jug1 is empty, fill it
    if jug1 == 0:
        jug1 = m
        print(f"Fill Jug1: ({jug1}, {jug2})")

    # Rule 2: If jug2 is full, empty it
    elif jug2 == n:
        jug2 = 0
        print(f"Empty Jug2: ({jug1}, {jug2})")

    # Rule 3: Pour water from jug1 to jug2
    else:
        transfer = min(jug1, n - jug2)
        jug1 -= transfer
        jug2 += transfer
        print(f"Pour Jug1 → Jug2: ({jug1}, {jug2})")

