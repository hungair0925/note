class BookShelf:
    def __init__(self, name):
        self.bk_sh = {}
        self.name = name
    
    def __str__(self):
        message = "本棚[{0}]".format(self.name)
        return message
    
    def add_book(self, title, author):
        self.bk_sh[title] = author
        print("追加したよ(￣･ω･￣)")
    
    def list_book(self):
        if len(self.bk_sh) == 0:
            print("棚には何も追加されていません")
        else:
            print("{0:<10}| {1:<15}".format("Title", "Author"))
            print("{0}".format("-"*25))
            for title, author in self.bk_sh.items():
                print("{0}| {1}".format(title, author))
            print("{0}".format("-"*25))
            
    def remove_book(self, title):
        del_flag = int(input("削除していいの(´･ω･`)?[0:NG/1:OK]"))
        if del_flag:
            rm_book_author = self.bk_sh.pop(title)
            print("{0}(著):{1}を削除しました".format(rm_book_author, title))
        else:
            pass
 #インスタンス
shelf = BookShelf("お気に入り") #インスタンスしたオブジェクトの名前
print(shelf) #追加
shelf.add_book("論語と算盤", "渋沢栄一")
shelf.add_book("脳・心・人工知能", "甘利俊一")
shelf.add_book("留魂録", "吉田松陰") #一覧表示
shelf.list_book() #削除
shelf.remove_book("留魂録")
