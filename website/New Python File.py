from flask import Flask, render_template, flash, request
app = Flask(__name__)
app.secret_key = "jnjn_8787DGFHDG"

@app.route('/')
def index():
   flash("1290")
   return render_template('index.html')

@app.route('/sammud', methods=["POST", "GET"])
def test():
   flash(str(request.form["sammud"]))
   return render_template('index.html')
   

if __name__ == '__main__':
   app.run()