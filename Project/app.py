from flask import *
import pandas as pd
import os

app = Flask(__name__)

app.secret_key = '1234'

def load_users():
    df = pd.read_csv('data.csv')
    return dict(zip(df.username, df.password))
def get_data():
    df = pd.read_csv('main.csv')
    return df.to_dict('records')

users = load_users()

@app.route('/')
def root():
    return render_template("auth.html")

@app.route('/auth/', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for("home"))
    else:
        return render_template("auth.html", data={"type": "error"})

@app.route('/home')
def home():
    return render_template("index.html", data=get_data())

@app.route('/save', methods=['GET', 'POST'])
def save():
    data = {
        "name": request.form.get('name'),
        "lastname": request.form.get('lastname')
    }
    df_new = pd.DataFrame([data])
    if os.path.exists("./main.csv"):
        df_existing = pd.read_csv("./main.csv")
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.drop_duplicates(inplace=True)
    else:
        df_combined = df_new
    df_combined.to_csv("./main.csv", index=False)
    return redirect(url_for("home"))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('root'))

@app.route('/delete/<name>', methods=['GET'])
def delete(name: str):
    df_existing = pd.read_csv("./main.csv")
    df = df_existing[df_existing['name'] != name]
    df.to_csv("./main.csv", index=False)
    return redirect(url_for("home"))
    
if __name__ =="__main__":
    app.run(host="0.0.0.0", port=99, debug=True)