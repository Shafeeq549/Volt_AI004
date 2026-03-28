import json
import time
import random
import os

def friend():
    choice_friend = ["Bro", "Sir", "Buddy"]
    return random.choice(choice_friend)

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

def formal():
    choice_formal = ["Sir", "Partner"]
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
        "Cozy Whisker",
        "Fluffy Companion"
    ]
    return random.choice(choice_friend)

class Personal_Note:
    def __init__(self):
        self.nama_file = "notes.json"
        self.data = {}

    def buka_file(self):
        try:
            with open(self.nama_file, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

    def input_file(self):
        isi_file = input("Insert note: ")
        nama_file = input("Insert note title: ")
        self.data[nama_file] = isi_file
        self.simpan_file()  # otomatis simpan setelah input

    def simpan_file(self):
        with open(self.nama_file, "w") as file:
            json.dump(self.data, file, indent=4)

    def GPIO_notef(self):
        nomor_gpio = int(input("Insert GPIO number: "))
        fungsi_gpio = input(f"Insert note for GPIO{nomor_gpio}")
        self.data[f"GPIO{nomor_gpio}"] = fungsi_gpio
        self.simpan_file()

    def nama_projek(self):
        nama_projek = input(f"Insert project title")
        return nama_projek

    def search_file(self, keyword=None):
        for nama, isi in self.data.items():
            if keyword is None or keyword.lower() in nama.lower() or keyword.lower() in isi.lower():
                print(f"{nama}: {isi}")
                time.sleep(10)

    def Arduino_notef(self):
        jenis_pin = input("Pin type: ")
        time.sleep(1)
        nomor_pin = input(f"Insert pin Name or Number {friend_cat()}: ")
        fungsi_arduino = input(f"Insert Note for {jenis_pin}{nomor_pin} {friend_cat()}: ")
        self.data[f"{jenis_pin}{nomor_pin} "] = fungsi_arduino
        self.simpan_file()

    def delete_file(self, nama_file):
        if nama_file in self.data:
            check = input(f"Are you sure {friend}")
            if check == "yes":
                del self.data[nama_file]
                self.simpan_file()
                print(f"Note '{nama_file}' succesfully deleted {friend_cat()}.")
            else:
                return "Canceled"

        else:
            print(f"Cant find {nama_file} {friend_cat()}")

class Smart_Note:
    def __init__(self):
        self.nama_file = "notes.json"
        self.data = {}

    def buka_file(self):
        try:
            with open(self.nama_file, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

    def input_file(self):
        isi_file = input("Insert note: ")
        nama_file = input("Insert note title: ")
        self.data[nama_file] = isi_file
        self.simpan_file()  # otomatis simpan setelah input

    def simpan_file(self):
        with open(self.nama_file, "w") as file:
            json.dump(self.data, file, indent=4)

    def search_file(self, keyword=None):
        for nama, isi in self.data.items():
            if keyword is None or keyword.lower() in nama.lower() or keyword.lower() in isi.lower():
                print(f"{nama}: {isi}")
                time.sleep(10)

    def GPIO_notef(self):
        nomor_gpio = int(input("Insert GPIO number: "))
        fungsi_gpio = input(f"Insert gpio note {nomor_gpio}")
        self.data[f"GPIO{nomor_gpio}"] = fungsi_gpio
        self.simpan_file()


    def delete_file(self, nama_file):
        if nama_file in self.data:
            check = input(f"Are you sure {friend}")
            if check == "yes":
                del self.data[nama_file]
                self.simpan_file()
                print(f"Note '{nama_file}' berhasil dihapus {formal()}.")
            else:
                return "Canceled"

        else:
            print(f"Note '{nama_file}' tidak ditemukan.")

    def formal_delete_file(self, nama_file):
        if nama_file in self.data:
            check = input(f"Are you sure {friend}")
            if check == "yes":
                del self.data[nama_file]
                self.simpan_file()
                print(f"Note '{nama_file}' succesfully deleted {formal()}.")
            else:
                return "Canceled"

        else:
            print(f"Note '{nama_file}' cant be found {formal()}.")

class Folder_Note:
    def __init__(self):
        self.nama_folder1 = "folder_A"
        self.nama_folder2 = "folder_B"
        self.folder = None
        self.nama_note = None
        self.nama_file = "folder.json"
        self.board = None
        self.data = {}
        self.buka_file()

    def simpan_file(self):
        with open(self.nama_file, "w") as file:
            json.dump(self.data, file, indent=4)

    def buka_file(self):
        if os.path.exists(self.nama_file):
            with open(self.nama_file, "r") as file:
                self.data = json.load(file)
        else:
            self.data = {}

    def lihat_folder(self, folder_name=None):
        if folder_name is None:
            folder_name = self.folder
        if folder_name in self.data:
            print(json.dumps(self.data[folder_name], indent=4))
        else:
            print(f"Folder '{folder_name}' not found.")

    def hapus_note(self, folder_name, note_name):
        # auto convert folder letter to folder name
        if folder_name.upper() == "A":
            folder_name = self.nama_folder1
        elif folder_name.upper() == "B":
            folder_name = self.nama_folder2

        if folder_name in self.data:
            if note_name in self.data[folder_name]:
                check = input(f"Are you sure you want to delete '{note_name}' from {folder_name}? (yes/no): ")
                if check.lower() == "yes":
                    del self.data[folder_name][note_name]
                    self.simpan_file()
                    print(f"Note '{note_name}' deleted from {folder_name} {friend_cat()}.")
                else:
                    print(f"Canceled {friend_cat()}.")
            else:
                print(f"Note '{note_name}' not found in '{folder_name}'.")
                print(f"Available notes: {list(self.data[folder_name].keys())}")
        else:
            print(f"Folder '{folder_name}' not found.")

    def pilih_folder(self):
        pilih_folder = input(f"Which folder you want {friend()}? (A/B): ")
        if pilih_folder.upper() == "A":
            self.folder = self.nama_folder1
        else:
            self.folder = self.nama_folder2
        if self.folder not in self.data:
            self.data[self.folder] = {}

    def pilih_board(self):
        pilihan_board = input(f"Select your board {friendly()}: (arduino/raspberry) ")
        if pilihan_board.lower() == "arduino":
            self.board = "arduino"
        elif pilihan_board.lower() == "raspberry":
            self.board = "raspberry"

    def pilih_pin(self):
        nomor_pin = int(input(f"Select your pin {friendly()}: "))
        if self.board == "arduino":
            jenis_pin = input(f"What's the pin type {friendly()}? (digital/analog) ")
            self.nama_note = f"{jenis_pin}{nomor_pin}"
        elif self.board == "raspberry":
            self.nama_note = f"GPIO{nomor_pin}"

    def input_note(self):
        input_note = input(f"What's the purpose of this pin {friendly()}? ")
        if self.folder not in self.data:
            self.data[self.folder] = {}
        self.data[self.folder][self.nama_note] = input_note
        self.simpan_file()
        print(f"{self.nama_note}: {input_note} saved in {self.folder}")
        time.sleep(1)
