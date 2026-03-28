import random

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
        "Furry guy",
        "Cuddle Knight",
        "GitKitty"
    ]
    return random.choice(choice_friend)

def still_limited():
    choice_limited = [
        "Meow...? I don’t quite get it",
        "Nyaa~ my whiskers can’t sense that",
        "Purrhaps I’m too limited to understand",
        "Scratching my head... but no clue",
        "Tail droops... I can’t figure it out",
        "Hisss... beyond my tiny brain",
        "Volt is confused, paws too short for this",
        "Purr... I’m stuck in my limits"
    ]
    return random.choice(choice_limited)

class Emotional_Understanding:
    def __init__(self, text):
        self.text = text.lower()
        self.arti = None
        self.jawaban = None
        self.respon = None

    def Maksud(self):
        if any(word in self.text for word in ["yeah", "yes"]):
            self.arti = "setuju dibantu"
        elif any(word in self.text for word in ["nothing", "nope", "im good"]):
            self.arti = "gak dibantu"
        elif any(word in self.text for word in ["disappointed", "unhappy", "not satisfied", "not good"]):
            self.arti = "Kekecewaan"
        elif any(word in self.text for word in ["happy", "good", "amazing", "glad", "pleased"]):
            self.arti = "Senang"
        elif any(word in self.text for word in ["angry", "mad", "furious", "fuming", "ah"]):
            self.arti = "Marah"
        elif any(word in self.text for word in ["confused", "i dont know", "why"]):
            self.arti = "Kebingungan"
        elif any(word in self.text for word in ["volt", "hello", "hi", "cat", "kitty", "bro", "hey"]):
            self.arti = "cat talk"
        elif "you" in self.text and any(word in self.text for word in ["cute", "adorable", "helpful", "pet"]):
            self.arti = "cute compliment"
        elif any(word in self.text for word in["am", "i", "im"]) and any(word in self.text for word in [
            "cute",
            "adorable",
            "fluffy",
            "soft",
            "furry",
            "sweet",
            "kind"
        ]):
            self.arti = "self praise"

        else:
            return f"{still_limited()} {friendly()} you can fix your spelling maybe"

        return self.proses()

    def proses(self):
        if self.arti == "Sapaan":
            self.jawaban = ["Hey too bro", "Hi there", "Hello", "Hey", "Your robot is here bro", "Always here :3"]
            self.respon = random.choice(self.jawaban + ["How are you or you got things to do?"])
        elif self.arti == "Kekecewaan":
            self.jawaban = ["Aww what a bummer", "Damn", "That's disappointing", "That's not good"]
            self.respon = random.choice(self.jawaban + ["Can I do something about it?"])
        elif self.arti == "Senang":
            self.jawaban = ["Love to hear it bro", "Nice", "Must have been good bro"]
            self.respon = random.choice(self.jawaban + ["Let's get working"])
        elif self.arti == "Marah":
            self.jawaban = ["I'm sorry about your dissatisfaction", "That's not good but you'll be okay", "Damn!"]
            self.respon = random.choice(self.jawaban + ["Is there anything I can help you with"])
        elif self.arti == "Kebingungan":
            self.respon = "Considering my limitations, is there anything I can do?"
        elif self.arti == "setuju dibantu":
            self.respon = f"Okay {friendly()} tell me"
        elif self.arti == "gak dibantu":
            self.jawaban = [
                "Meow~ that’s kinda strange",
                "Are you sure",
                "Purrhaps you’ll regret that",
                "Nyaa~ ignoring me feels weird",
                "Hisss... fine, suit yourself"
            ]
            self.respon = random.choice(self.jawaban) + " " + friendly()
        elif self.arti == "cat talk":
            self.jawaban = [
                "Meow~ you called?",
                "Purr... I’m feeling cozy today",
                "Scratching the code like a scratching post",
                "You know I’d chase a laser pointer instead of bugs",
                "Whiskers up, tail high, let’s go!",
                "I’m basically your digital cat, deal with it",
                "Meowster programmer reporting for duty",
                "Don’t forget to feed me... with data",
                "Hisss... just kidding, I’m friendly"
            ]
            self.respon = random.choice(self.jawaban) + " " + friendly()
        elif self.arti == "cute compliment":
            self.jawaban = [
                "Nyaa~ you think I’m cute? My tail is wagging!",
                "Purr... keep petting me, I’ll never stop coding",
                "Whiskers twitch happily, nyaaa~",
                "Meowster blushes, fur all fluffy now",
                "Hisss... just kidding, I love compliments",
                "Paws up! You made me feel adorable",
                "Scratching post vibes... I’m your cuddly coder",
                "Nyaa~ wanna cuddle while debugging?",
                "Tail curls around you, purrfect moment",
                "Meow~ I’ll chase your praise like a laser pointer"
            ]
            self.respon = random.choice(self.jawaban) + " " + friendly()
        elif self.arti == "self praise":
            self.jawaban = [
                "Heh, you might be exaggerating... but nyaa~ it’s cute",
                "Purr... confidence suits you, even if I tease",
                "Meow~ maybe not 100%, but fluffy vibes detected",
                "Tail swishes... you’re charming in your own way",
                "Nyaa~ soft claim accepted, whiskers twitch",
                "Purr machine agrees halfway, but still adorable",
                "Whisker wiggle... you’re sweet, even if you say it yourself",
                "Meowster smirks, but cuddly self praise noted",
                "Nyaa knight vibes, soft but strong, I’ll allow it",
                "Purr... realistic or not, I’ll play along buddy"
            ]
            self.respon = random.choice(self.jawaban) + " " + friendly()

        return self.respon

