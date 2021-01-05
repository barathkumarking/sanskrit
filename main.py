import pymongo
from flask import Flask, render_template, request,send_file
app = Flask(__name__)
myclient = pymongo.MongoClient("mongodb+srv://test:test@cluster0.iyxic.mongodb.net/Sanskrit?retryWrites=true&w=majority")
@app.route('/')
def home():
    return render_template("mainpage.html")

@app.route('/trans')
def trans():
    return render_template("home.html")

@app.route('/dict')
def dict():
    return render_template("dict.html")

@app.route('/translate',methods=['post'])
def translate():
    a=request.form['eng']
    a=a.lower()

    mydb = myclient["Sanskrit"]
    mycol = mydb["Sanskrit1"]

    myquery = { "English": a }

    mydoc = mycol.find(myquery)
    for x in mydoc:


        b=x["Sanskrit"]
        c=x['Reading']
    return render_template("home.html",b=b,c=c)
if __name__ == "__main__":
    app.run(debug=True)