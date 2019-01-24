from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def showBoxes():
    return render_template("checkerboard.html", rows=int(8/2), cols=int(8/2))

@app.route('/<x>/<y>')
def showBoxes1(x,y):
    return render_template("checkerboard.html", rows=int(int(x)/2), cols=int(int(y)/2))



if __name__=="__main__":
    app.run(debug=True)
