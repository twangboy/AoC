with open("day1-input.txt", "r") as f:
    expenses = f.read().splitlines()

expenses = [int(x) for x in expenses]

stop = False
for exp_1 in expenses:
    if stop:
        break
    for exp_2 in expenses:
        if stop:
            break
        for exp_3 in expenses:
            if stop:
                break
            sum = exp_1 + exp_2 + exp_3
            if sum == 2020:
                print(exp_1 * exp_2 * exp_3)
                stop = True
