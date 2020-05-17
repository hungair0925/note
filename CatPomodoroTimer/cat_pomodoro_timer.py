from time import sleep
from os import system

class Timer():
    def __init__(self, minute):
        self.minute = minute
        self.message = "Count Up!"

    def count_every_minute(self):
        for i in range(self.minute, -1, -1):
            if i == 0:
                print(self.message)
                break
            print("{0}分..".format(i))
            sleep(60)
        
class CatPomodoroTimer(Timer):
    def __init__(self, set_num):
        self.set_num = set_num
        self.sound = "cat.mp3"

    def play_cat_voice(self, loop_num):
        for _ in range(loop_num):
            system("afplay {0}".format(self.sound))

    def count_25minute(self):
        self.minute = 25
        self.message= "にゃーん(休憩だよ-)"
        self.count_every_minute()
        self.play_cat_voice(3)
    
    def count_5minute(self):
        self.minute = 5
        self.message= "にゃーん(始めよ-)"
        self.count_every_minute()
        self.play_cat_voice(1)
    
    def count_pomodoro(self):
        for i in range(self.set_num):
            self.count_25minute()
            self.count_5minute()
        print("おつかれさま、お茶よ( ^-^)_旦")

if __name__ == "__main__":
    set_num = int(input("何ポモドロ回しますか?:"))
    cpt = CatPomodoroTimer(set_num)
    cpt.count_pomodoro()
