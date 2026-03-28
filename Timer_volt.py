import time

class Smart_Timer:
    def __init__(self):
        self.waktu = None
        self.satuan_waktu = None
        self.menit = None
        self.hour = None
        self.second = None

    def set_satuan(self, waktu=None):
        jenis_waktu = input("Select units for the timer (minute/hour/second): ").lower()
        if jenis_waktu in ["minute", "hour", "second"]:
            self.satuan_waktu = jenis_waktu
            self.set_waktu()

    def set_waktu(self):
        if self.satuan_waktu == "minute":
            self.waktu = int(input("Insert time in minutes: "))
            self.menit = self.waktu * 60
        elif self.satuan_waktu == "hour":
            self.waktu = int(input("Insert time in hours: "))
            self.hour = self.waktu * 3600
        elif self.satuan_waktu == "second":
            self.waktu = int(input("Insert time in seconds: "))
            self.second = self.waktu

    def run_timer_minute(self):
        run_menit = self.menit
        while run_menit > 0:
            print(run_menit)
            run_menit -= 1
            time.sleep(1)
        return "Minute timer is finished!"

    def run_timer_hour(self):
        run_hour = self.hour
        while run_hour > 0:
            print(run_hour)
            run_hour -= 1
            time.sleep(1)
        return "Hour timer is finished!"

    def run_timer_second(self):
        run_second = self.second
        while run_second > 0:
            print(run_second)
            run_second -= 1
            time.sleep(1)
        return "Second timer is finished!"
