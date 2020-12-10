# https://adventofcode.com/2020/day/2
with open("day2-input.txt", "r") as f:
    passwords = f.read().splitlines()

valid = 0
for password in passwords:
    rule, pwd = password.split(": ")
    rng, letter = rule.split()
    pos1, pos2 = rng.split("-")
    pos1 = int(pos1) - 1
    pos2 = int(pos2) -1
    if pwd[pos1] == letter or pwd[pos2] == letter:
        if pwd[pos1] == letter and pwd[pos2] == letter:
            pass
        else:
            valid += 1

print(valid)