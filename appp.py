from flask import Flask,request,jsonify
app=Flask(__name__)
data=[
    {"id":1,'name':'maruf','message':"this is first page"},
    {"id":2,'name':'mehar','message':"this is second page"},
]
# this is home page 
@app.route('/')
def home():
    return "this is home page"
# retrive all data from data list
@app.route('/index',methods=['GET'])
def index():
    return jsonify(data)
# retrive one id from data
@app.route('/index/<int:score>',methods=['GET'])
def indivisual(score):
    ind=next((ind for ind in data if ind['id']==score),None)
    if ind is None:
        return jsonify({'earror':'items not found'})
    return jsonify(ind)
# add new id in data list
app.route('/index',methods=["POST"])
def post():
    if not request.json or not 'name' in request.json:
        return jsonify({'earror':'items not found'})
    new={
        'id': data[-1]['id']+1 if data else 1,
        'name':request.json['name'],
        'message':request.json['message']
                }
    data.append(new)
    return jsonify(new)
# now update the itmes with put method
@app.route('/index/<int:score>',methods=['PUT'])
def update(score):
    ind=next((ind for ind in data if ind['id']==score),None)
    if ind is None:
        return jsonify({'earror':'items not found'})
    ind['name']=request.json.get('name',ind['name'])
    ind['message']=request.json.get('message',ind['message'])
    return jsonify(ind)
@app.route('/index/<int:score>',methods=['DELETE'])
def delete(score):
    global int
    int=[int for int in data if int["id"]!=score]
    return jsonify({"result":"item deleted"})


if __name__=='__main__':
    app.run(debug=True)