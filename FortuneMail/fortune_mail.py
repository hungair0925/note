from getpass import getpass
from random import randint
from datetime import datetime
from smtplib import SMTP
from smtplib import SMTPAuthenticationError
from email.mime.text import MIMEText
from email.utils import formatdate
 #設定情報
HOST = "smtp.gmail.com"
PORT = 587 #入力情報
user_address = input("gmailのアドレス:")
password = getpass("gmailのパスワード:")
to_email = input("送り先のメールアドレス:") #メッセージ内容作成
today = datetime.now().strftime("%Y/%m/%d")
mikuji = ["大吉", "中吉", "小吉", "末吉", "n吉"]
items = ["傘", "コーヒー", "聖書", "オライリーの分厚い本", "権力"]
content = f"運勢:{mikuji[randint(0, len(mikuji) - 1)]}\nラッキーアイテム:{items[randint(0, len(items) - 1)]}"

message = MIMEText(content)
message["Subject"] = f"{today}の運勢"
message["From"] = user_address
message["To"] = to_email
message["Date"] = formatdate()

from_email = user_address
to_list = [to_email]

gmail_smtp = SMTP(HOST, PORT) #TLSでsmtp接続(以降のコマンド暗号化)
gmail_smtp.starttls()
try:
    gmail_smtp.login(user_address, password)
    gmail_smtp.sendmail(from_email, to_list, message.as_string())
    print("--送信完了--")
except SMTPAuthenticationError:
    print("ログインに失敗しました。")
finally:
    gmail_smtp.quit()
