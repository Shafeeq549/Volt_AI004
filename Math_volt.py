import numexpr
import time
import random

def formal():
    choice_formal = ["Sir", "Partner", "User", "Friend"]
    return random.choice(choice_formal)

def friend_cat():
    choice_friend = [
        "Meowster Pal",
        "Nyaa~ Fluffy Buddy",
        "Purrfect Friend",
        "Whisker Mate",
        "Furry Bro",
        "Tail Wag Buddy",
        "Claw-some Friend",
        "Soft Paw Pal",
        "Nyaa~ Cozy Whisker",
        "Fluffy Companion"
    ]
    return random.choice(choice_friend)

def happy_help():
    choice_happy_help = [
        "Purr~ I’m happy to help!",
        "Meowster at your service!",
        "Nyaa~ let’s solve this together",
        "Whiskers up, tail high, ready to go!",
        "Scratching the numbers like a post",
        "Purrhaps I can make this easy for you",
        "Meow~ Volt is on the case",
        "Laser-focused like chasing a pointer",
        "Nyaa buddy, I’ve got your back,",
        "Purrfect time to calculate!"
    ]
    return random.choice(choice_happy_help)

class Personal_Asistant:
    def __init__(self, text):
        self.text = text.lower()
        self.asistant = None
        self.expr = None

    def bantuan(self):
        friendly_words = ["bro", "buddy", "sir", "please", "cat", "volt", "hey"]
        math_words = ["math", "number", "much", "calculator"]

        if any(word in self.text for word in math_words):
            self.asistant = "math"
            # kalau tidak ada kata ramah, jawab biasa
            if not any(word in self.text for word in friendly_words):
                return f" the answer is{self.MATH()}"
            else:
                # kalau ada kata ramah, jawab lebih friendly
                return f"{happy_help()} the answer is {self.MATH()} {friend_cat()}"

    def MATH(self):
        time.sleep(1)
        self.expr = input("Insert expression: ")
        try:
            return f"{numexpr.evaluate(self.expr)}"
        except Exception as e:
            return f"Error: {e} oh do it right next time {friend_cat()}"



class Formal_Asistant:
    def __init__(self, text):
        self.text = text.lower()
        self.asistant = None
        self.expr = None

    def bantuan_formal(self):
        math_words = ["math", "number", "much", "calculator"]
        if any(word in self.text for word in math_words):
            self.asistant = "math"
            return f"the answer is {self.MATH()}"

    def MATH(self):
        print(f"With pleasure {formal()}")
        time.sleep(1)
        self.expr = input("Insert expression: ")
        try:
            return f"{numexpr.evaluate(self.expr)}"
        except Exception as e:
            return f"Error: {e} Do it right next time {formal()}"
