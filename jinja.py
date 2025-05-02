from flask import Flask,render_template,request,redirect, url_for
app=Flask(__name__)
@app.route("/")
def flask():
    return "hello flask  maruf khan jddufidfgdjkduifhsjkb ehey"
@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f" hello {name}!"
    return render_template('form.html')
# varriable rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="passed"
    else:
        res="falled"
    return render_template('result.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="passed"
    else:
        res="failed"
    resu={ "score": score,"result":res}
    return render_template('result1.html',results=resu)
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method==['POST']:
        science=float(request.form['sci'])
        maths=float(request.form['mat'])
        c=float(request.form['c'])
        dt=float(request.form['dt'])
        total_score=(science+maths+c+dt)
    return redirect(url_for('successres',score=total_score))

if __name__=="__main__":
    app.run(debug=True)