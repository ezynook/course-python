from flask import *
import pandas as pd

app = Flask(__name__)

@app.route('/text')
def text():
    params = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque sit amet accumsan tortor. Nam vel enim id urna feugiat fermentum. Phasellus ut ligula nec libero sollicitudin dictum. Vestibulum vehicula dictum ex, nec dignissim eros blandit vel. Mauris quis dolor euismod, feugiat lacus at, vehicula elit. Donec tincidunt, nisl sed tempor convallis, augue felis dignissim dui, ac bibendum odio est eu lorem. Vivamus sodales, turpis id commodo efficitur, risus ante ullamcorper dolor, sed cursus metus nulla eget risus. Integer sit amet tortor id ligula euismod vehicula et nec nulla."
    return render_template("text.html", data=params)

@app.route('/list')
def list():
    params = [
        "apple", 
        "banana", 
        "cherry", 
        "date"
    ]
    
    return render_template("list.html", data=params)

@app.route('/dict')
def dict():
    params = {
        1: 'Python', 
        2: 'dictionary', 
        3: 'example'
    }

    return render_template("dict.html", data=params)

@app.route('/tuple')
def tuple():
    params = ("apple", "banana", "cherry", "date")
    return render_template("tuple.html", data=params)


@app.route('/file')
def file():
    with open("../File/Example.txt", "r") as file:
        content = file.readlines()
        return render_template("file.html", data=content)
    
@app.route('/excel')
def excel():
    df = pd.read_excel("../File/Example.xlsx")
    result = df.to_dict(orient='records')
    return render_template("excel.html", data=result)



if __name__ =="__main__":
    app.run(host="0.0.0.0", port=99, debug=True)