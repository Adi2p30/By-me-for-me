import time
print("TIMER HAI GUYS")
ans = ""
timer = 0
completed = 0
wrong = 0
right = 0
totaltime = 0
avgtime = 0
while ans != "X":

    if ans!= "P":
        if ans == "W":
            completed = completed + 1
            right = right + 1
            totaltime = totaltime + timer
            timer = 0
        elif ans == "L":
            completed = completed + 1
            wrong = wrong + 1
            totaltime = totaltime + timer
            timer = 0
        elif ans == "S":
            print(str(wrong) + " wrong\n" + str(right) + " right\n" + str(completed) + " completed")
            avgtime = totaltime/completed
            print(str(avgtime) + " is ur avg time")
        timer = timer + 1
        time.sleep(1)
        print(timer)
        ans = input("")
    else:
        print("You have paused your session!")
        print("Currently you have \n" + str(wrong) + " wrong\n" + str(right) + " right\n" + str(avgtime) + " is your average time per question\n")
if ans == "X":
    exit(0)

