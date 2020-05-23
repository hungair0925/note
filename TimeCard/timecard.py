from datetime import datetime

class TimeCard:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.end_time = None
        self.work_time = None
        self.push_time = 0

    def push(self):
        if self.push_time % 2 == 0:
            self.start_time = datetime.now()
        elif self.push_time % 2 == 1:
            self.end_time = datetime.now()
        self.push_time += 1
    
    def print_time(self):
        if self.push_time % 2 == 1:
            s_month = self.start_time.month
            s_day = self.start_time.day
            s_hour = self.start_time.hour
            s_minute = self.start_time.minute
            print("{0}月{1}日{2}時{3}分".format(s_month, s_day, s_hour, s_minute))
        elif self.push_time % 2 == 0:
            e_month = self.end_time.month
            e_day = self.end_time.day
            e_hour = self.end_time.hour
            e_minute = self.end_time.minute
            print("{0}月{1}日{2}時{3}分".format(e_month, e_day, e_hour, e_minute))

    def calc_work_time(self):
        self.work_time = self.end_time - self.start_time

if __name__ == "__main__":
    while True:
        name = input("お名前を入力してください:")
        worker = TimeCard(name)
        for _ in range(2):
            mode = int(input("1:打刻 "))
            if mode:
                worker.push()
                worker.print_time()
        worker.calc_work_time()
        print("{0}さんの労働時間:{1}".format(worker.name, worker.work_time))
        flag = input("1:続ける/0:終了 ")
        if flag == 1:
            continue
        elif flag == 0:
            break
