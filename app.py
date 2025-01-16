from flask import Flask, render_template, request
from complementary_color import CColor
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/opcolor")
def opcolor():
    color = "#FFFFFF"
    if request.args.get("color"):
        color = request.args.get("color")
    opcolor = CColor(color)        
    return render_template("CColor.html",opcolor = opcolor,color = color)

@app.route("/modern-opcolor")
def Mopcolor():
    color = "#FFFFFF"
    if request.args.get("color"):
        color = request.args.get("color")
    opcolor = CColor(color)        
    return render_template("CColor_modern.html",opcolor = opcolor,color = color)
        

    
