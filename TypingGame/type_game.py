from bs4 import BeautifulSoup
from random import sample
from time import time
import requests

class TypingGame:
    def __init__(self):
        #Python公式ドキュメント組み込み関数に関してのページ
        self.URL = "https://docs.python.jp/3/library/functions.html"
        #問題リスト
        self.question_list = []
        #出題数
        self.question_num = 10
        #正解数
        self.correct_num = 0
        #タイポリスト
        self.mistake_list = []
        #開始時間
        self.start_time = 0
        #終了時間
        self.end_time = 0

  #問題生成メソッド
    def generate_question(self):
        res = requests.get(self.URL)
        #文字コードを変換
        res.encoding = res.apparent_encoding
        #レスポンスのテキスト情報をhtmlに解釈する
        soup = BeautifulSoup(res.text, "html.parser")
        #組み込み関数一覧が表示されているテーブルタグ全体の情報を抜き出す
        built_in_func_table = soup.find_all("table", class_="docutils", limit=1)
        #リストからhtmlの要素を取り出す
        built_in_func_table = built_in_func_table[0]
        #テーブル内の組み込み関数のタグを取得
        built_in_func_tags = built_in_func_table.find_all("span", class_="pre")
        #問題リストに組み込み関数の文字列を格納
        for tag in built_in_func_tags:
            self.question_list.append(tag.text)

    #問題表示
    def show_question(self):
        question = sample(self.question_list, 1)
        return question[0]
    
    #判定メソッド
    def judge(self, question):
        user_input = input("=> ")
        if question == user_input:
            print("Great!")
            self.correct_num += 1
        else:
            print("Boo!")
            self.mistake_list.append(question)
    
   #結果表示
    def show_result(self):
        play_time = round(self.end_time - self.start_time, 2)
        accuracy = round(self.correct_num / self.question_num, 1) * 100
        print("---結果発表---")
        print("正答率:{0}%".format(accuracy))
        print("かかった時間{0}秒".format(play_time))
        if len(self.mistake_list) == 0:
            print("パーフェクト!")
        else:
            print("--間違えた問題---")
            for mistake in self.mistake_list:
                print(mistake)
    
    #ゲーム処理
    def main(self):
        #開始時間計測
        self.start_time = time()
        #出題と判定の繰り返し
        for _ in range(self.question_num):
            question = self.show_question()
            print("{0}".format(question))
            self.judge(question)
        #終了時間計測
        self.end_time = time()
        self.show_result()

if __name__ == "__main__":
    game = TypingGame()
    game.generate_question()
    print("組み込み関数Pythoタイピングゲーム")
    while 1:
        game_flag = int(input("1:スタート/0:終了 "))
        if game_flag == 1:
            game.main()
        else:
            break
