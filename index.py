from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    #done
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run()
