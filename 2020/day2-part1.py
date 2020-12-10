# https://adventofcode.com/2020/day/2
with open("day2-input.txt", "r") as f:
    passwords = f.read().splitlines()

valid = 0
for password in passwords:
    rule, pwd = password.split(": ")
    rng, letter = rule.split()
    lower, upper = rng.split("-")
    count = sum(map(lambda i: i == letter, pwd))
    if int(lower) <= count <= int(upper):
        valid += 1

print(valid)