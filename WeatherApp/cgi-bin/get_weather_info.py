#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import cgi
import requests
 #フォームから入力された値を取得する関数(返すデータ型:辞書型)
form = cgi.FieldStorage()
city_name = form["city_name"].value

def weather_info(city_name):
    app_id = "こちらにはで取得したidを入れてください"
    URL = "https://api.openweathermap.org/data/2.5/weather?q={0},jp&units=metric&lang=ja&appid={1}".format(city_name, app_id)
    IMAGE_URL = "https://openweathermap.org/img/w/"
    response = requests.get(URL)
    data =  response.json()
    #天気情報
    weather = data["weather"][0]["description"]
    #天気アイコン
    weather_icon = data["weather"][0]["icon"]
    #最高気温
    temp_max = data["main"]["temp_max"]
    #最低気温
    temp_min = data["main"]["temp_min"]
    #湿度
    humidity = data["main"]["humidity"]
    #imgタグに埋め込む画像パス
    img_src = IMAGE_URL + weather_icon + ".png"

    context = {"weather": weather, 
               "temp_max":str(temp_max) + "度",
               "temp_min": str(temp_min) + "度", 
               "humidity": str(humidity) + "%",
               "img_src": img_src}

    return context

context = weather_info(city_name)

html_body = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>{0} Weather Today</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
    <div class="container">
    <h1 class="text-center" style="color:white; background-color:skyblue">今日の{0}のお天気</h1>
    <table class="table">
        <tr><td></td><td><img src="{1}" alt="weather_image" class="img-thumbnail"></td></tr>
        <tr><td>天気</td><td>{2}</td></tr>
        <tr><td style="color:#f33;">最高気温</td><td style="color:#f33;">{3}</td></tr>
        <tr><td style="color:#33f;">最低気温</td><td style="color:#33f;">{4}</td></tr>
        <tr><td style="color:#696969">湿度</td><td style="color:#696969">{5}</td></tr>
    </table>
    </div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
""".format(city_name,
           context["img_src"],
           context["weather"], 
           context["temp_max"], 
           context["temp_min"], 
           context["humidity"])
 #HTMLファイルを出力する旨を伝える
print("Content-type: text/html") #HTMLファイルの出力
print(html_body)
