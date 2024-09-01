from flask import Flask, render_template
from datetime import datetime
from script import script_stock


# print(__name__)

app = Flask(__name__)
books = {
    1: {
        "name": "Python book",
        "price": 299,
        "image_url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348",
    },
    2: {
        "name": "Java book",
        "price": 399,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348",
    },
    3: {
        "name": "C# book",
        "price": 499,
        "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348",
    },
    4: {
        "name": "Django book",
        "price": 1499,
        "image_url": "https://th.bing.com/th/id/OIP.B7eXLWyjaHmn8GYTkhG0OwHaEK?rs=1&pid=ImgDetMain",
    },
}


@app.route("/stocks")
def get_stocks():
    datas = script_stock()

    return render_template("stocks.html", stocks=datas)


# 程式練習
@app.route("/bmi/name=<name>&height=<h>&weight=<w>")
def get_bmi(name, h, w):
    try:
        bmi = round(eval(w) / (eval(h) / 100) ** 2, 2)
        return f"<h1><span style='color:blue'>姓名:{name}</span>身高:{h}體重:{w}BMI:{bmi}</h1>"
    except Exception as e:
        print(e)
    return "<h2>輸入數值不正確</h2>"


@app.route("/sum/x=<x>&y=<y>")  # <>代表外部傳進來的名稱
def my_sum(x, y):
    # 參數不正確，請輸出參數錯誤(try+except)
    try:
        z = eval(x) + eval(y)
        return f"{x}+{y}={z}"
    except Exception as e:
        print(e)
    return "<h2>請重新輸入</h2>"


@app.route("/book/<int:id>")
def show_book(id):
    # 輸出有書 <h1>第一本書:xxx</h1>
    # 或無此編號
    if id not in books:
        return f"<h2 style='color:red'>無此編號:{id}</h2>"

    return f"<h1>第{id}本書:{books[id]}</h1>"


@app.route("/books")
def show_books():
    print(books)

    for key in books:
        print(books[key])
    return render_template("books.html", books=books)


@app.route("/")  # 即將宣告首頁的意思
def index():
    today = datetime.now()
    # return f"<h1>Hello Flask!<br>{today}</h1>"
    name = "Peggy"
    return render_template("index.html", date=today, name=name)


app.run(debug=True)  # 加debug=True是為了在開發時測試，方便即時反應，實際發佈時要拿掉
