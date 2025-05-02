from flask import Flask
app=Flask(__name__)
@app.route("/")
def welcome():
    return "welcometo the best flask cource  flask cource"
if __name__=="__main__":
    app.run(debug=True)