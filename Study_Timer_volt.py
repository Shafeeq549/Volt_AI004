import time
import random

def servant():
    choice_servant = ["Sir", "User", "Buddy", "Friend"]
    return random.choice(choice_servant)

def friendly():
    choice_friend = [
        "Whisker King",
        "Purr Prince",
        "Fluffy Tail",
        "Meowlord",
        "Code Claw",
        "Laser-Chaser Hero",
        "Furball Champ",
        "Kitty Commander",
        "Tail-Swish Bro",
        "Meowster Supreme",
        "Purr Paladin",
        "Clawtastic Friend",
        "Snuggle Cat",
        "Whisker Wizard",
        "Pawgrammer",
        "Furry friend",
        "Cuddle Knight",
        "GitKitty"
    ]
    return random.choice(choice_friend)

class Pomodoro_timer:
    def __init__(self):
        self.study_time = 0
        self.rest_time = 0
        self.run_time = 0
    def start_study(self):
        self.study_time = int(input(f"How many minutes do you want to study {friendly()}?"))
        time.sleep(1)
        self.rest_time = int(input(f"And how many minutes do you want to rest in {self.study_time}?"))
        self.run_time = self.study_time - self.rest_time
        if self.rest_time <= 3:
            print(f"Well that's kinda short {friendly()} but OK")

    def run_timer(self):
        print(f"Start study session {friendly()}")
        while self.run_time > 0:
            print(f"{self.run_time} Min Remaining")
            self.run_time -= 1
            time.sleep(60)

        print(f"Study session is finished {friendly()}")

    def start_study_formal(self):
        self.study_time = int(input(f"How many minutes do you want to study {servant()}?"))
        time.sleep(1)
        self.rest_time = int(input(f"And how many minutes do you want to rest in {self.study_time}?"))
        self.run_time = self.study_time - self.rest_time
        if self.rest_time <= 3:
            print(f"Well that's kinda short {servant()} but OK")

    def run_timer_formal(self):
        print(f"Start study session {servant()}")
        while self.run_time > 0:
            print(f"{self.run_time} Min Remaining")
            self.run_time -= 1
            time.sleep(60)

        print(f"Study session is finished {servant()}")

