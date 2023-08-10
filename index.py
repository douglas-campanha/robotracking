from flask import Flask, render_template

app = Flask(__name__)

#cria a nova página do site
@app.route('/')
def homepage():
     return render_template("homepage.html")

if __name__ == "__main__":
   app.run(debug=True)







