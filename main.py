import random
import time
from EU_volt import Emotional_Understanding
from Math_volt import Personal_Asistant, Formal_Asistant
from Note_volt import Smart_Note, Personal_Note, Folder_Note
from Timer_volt import Smart_Timer
from Study_Timer_volt import Pomodoro_timer

def apreciation():
    if any(word in text_input.lower() for word in ["help", "please", "volt"]):
        choice_pleasure = [
            "Oh ok",
            "Oh of course",
            "Anything for you!",
            "Sure thing!",
            "On it!",
            "Always happy to help!",
            "You got it!",
            "Of course, no problem!",
            "Right away!",
            "Consider it done!",
            "Happy to help!",
            "Leave it to me!",
            "No worries at all!",
            "Say no more!",
            "Absolutely!",
        ]
        print(f"{random.choice(choice_pleasure)} {friendly()} ")

def servant():
    return random.choice(["With pleasure", "No problem", "Got you", "Wait a second"])

def friendly():
    choice_friend = [
        "Whisker Buddy",
        "Purr Pal",
        "Fluffy Friend",
        "Meow Mate",
        "Claw Companion",
        "Laser Chaser",
        "Furball Friend",
        "Kitty Captain",
        "Tail-Swish Pal",
        "Meowster",
        "Snuggle Cat",
        "Whisker Wizard",
        "Paw Pal",
        "Furry Friend",
        "Cuddle Cat",
        "GitKitty"
    ]
    return random.choice(choice_friend)

def friend():
    return random.choice(["Bro", "Buddy", "Silly cat guy"])


def welcome():
    return random.choice(["Hello", "Welcome back", "Well who's back", "RAWR", "Hey"])


def formal_welcome():
    return random.choice(["Welcome", "Greetings", "Good day", "Salutations", "Hello there"])


def formal():
    return random.choice(["Sir", "Partner", "User", "Friend"])


def jumlah_run(run_count):
    if run_count < 1:
        return input(f"Is there something you want me to do {friend()}? ")
    else:
        return input(f"Is there anything else you want me to help you {friend()}? ")


# ===== Main Program =====
run_count = 0
start = input("start: ")

if start == "004":
    sudah_welcome = False
    while True:
        # Sambutan pertama
        if not sudah_welcome:
            print(f"{welcome()} {friend()}")
            sudah_welcome = True

        # Bedakan pertanyaan pertama dan selanjutnya
        if run_count == 0:
            text_input = input(f"What can I help you {friend()}? ")
        else:
            text_input = input("Is there anything else I can help you with? ")
        run_count += 1

        # ===== Exit =====
        if text_input.lower() == "exit":
            print("Program selesai.")
            break

        # ===== Math Help =====
        elif "math" in text_input.lower():
            asisten_math = Personal_Asistant(text_input)
            apreciation() # Apresication if we asked nicely
            time.sleep(1)
            print(f"{servant()} {friend()}")
            time.sleep(1)
            print(asisten_math.bantuan())
            note = Personal_Note()
            note.buka_file()
            note.search_file()

        # ===== Note Input =====
        elif "note" in text_input.lower() and "input" in text_input.lower():
            apreciation() # Apresication if we asked nicely
            note = Personal_Note()
            note.buka_file()
            note.input_file()

        # ===== Note Delete =====
        elif "note" in text_input.lower() and "delete" in text_input.lower():
            apreciation() # Apresication if we asked nicely
            note = Personal_Note()
            note.buka_file()
            nama_file = input("Masukan nama note yang ingin dihapus: ")
            note.delete_file(nama_file)

        # ===== Note Raspberry =====
        elif "note" in text_input.lower() and "raspberry" in text_input.lower():
            apreciation() # Apresication if we asked nicely
            note = Personal_Note()
            note.buka_file()
            note.GPIO_notef()

        # ===== Note Arduino =====
        elif "note" in text_input.lower() and "arduino" in text_input.lower():
            apreciation() # Apresication if we asked nicely
            note = Personal_Note()
            note.buka_file()
            note.Arduino_notef()

        # ===== Timer =====
        elif "timer" in text_input.lower():
            apreciation() # Apresication if we asked nicely
            timer = Smart_Timer()
            timer.set_satuan(text_input)
            if timer.satuan_waktu == "minute":
                timer.run_timer_minute()
            elif timer.satuan_waktu == "hour":
                timer.run_timer_hour()
            elif timer.satuan_waktu == "second":
                timer.run_timer_second()

        # ===== Note Folder =====
                # ===== Note Folder Delete =====
        elif "folder" in text_input.lower() and "delete" in text_input.lower():
            apreciation()
            folder = Folder_Note()
            folder.buka_file()
            folder_name = input(f"Which folder you want {friendly()}: ")
            note_name = input(f"What note name you want me to delete {friendly()}: ")
            folder.hapus_note(folder_name, note_name)

        # ===== Note Folder Check =====
        elif "folder" in text_input.lower() and "check" in text_input.lower():
            apreciation()
            folder = Folder_Note()
            folder.buka_file()
            folder_name = input(f"Which folder you want me to check {friendly()}: ")
            folder.lihat_folder(folder_name)

        # ===== Note Folder Input =====
        elif "folder" in text_input.lower() and "input" in text_input.lower():
            apreciation()
            folder = Folder_Note()
            folder.pilih_folder()
            folder.pilih_board()
            folder.pilih_pin()
            folder.input_note()
        # ===== Pomodoro Timer ======
        elif "pomodoro" in text_input.lower() and "timer" in text_input.lower():
            apreciation() # Apresication if we asked nicely
            pomodoro = Pomodoro_timer()
            pomodoro.start_study()
            pomodoro.run_timer()

        # ===== Emotional Understanding =====
        else:
            emosi = Emotional_Understanding(text_input)
            print(emosi.Maksud())

else:
    sudah_welcome = False
    while True:
        # Sambutan pertama
        if not sudah_welcome:
            print(f"{formal_welcome()} {formal()}")
            sudah_welcome = True

        # Bedakan pertanyaan pertama dan selanjutnya
        if run_count == 0:
            text_input = input("What can I help you sir? ")
        else:
            text_input = input("Is there anything else I can help you with sir? ")
        run_count += 1

        # ===== Exit =====
        if text_input.lower() == "exit":
            print("Program selesai.")
            break

        # ===== Math Help Formal =====
        elif "math" in text_input.lower() and "help" in text_input.lower():
            asisten_math = Formal_Asistant(text_input)
            print(asisten_math.bantuan_formal())

        # ===== Note Check =====
        elif "note" in text_input.lower() and "check" in text_input.lower():
            note = Smart_Note()
            note.buka_file()
            note.search_file()

        # ===== Note Delete =====
        elif "note" in text_input.lower() and "delete" in text_input.lower():
            note = Smart_Note()
            note.buka_file()
            time.sleep(3)
            nama_file = input("Masukan nama note yang ingin dihapus: ")
            note.delete_file(nama_file)

        # ===== Note Input =====
        elif "note" in text_input.lower() and "input" in text_input.lower():
            note = Smart_Note()
            note.buka_file()
            note.input_file()

        # ===== Timer =====
        elif "timer" in text_input.lower() and "set" in text_input.lower():
            timer = Smart_Timer()
            timer.set_satuan(text_input)
            if timer.satuan_waktu == "minute":
                timer.run_timer_minute()
            elif timer.satuan_waktu == "hour":
                timer.run_timer_hour()
            elif timer.satuan_waktu == "second":
                timer.run_timer_second()

        elif "pomodoro" in text_input.lower() and "timer" in text_input.lower():
            pomodoro = Pomodoro_timer()
            pomodoro.start_study_formal()
            pomodoro.run_timer_formal()

        # ===== Note Microcontroller =====
        elif "note" in text_input.lower() and "microcontroller" in text_input.lower():
            note = Smart_Note()
            note.buka_file()
            note.GPIO_notef()
