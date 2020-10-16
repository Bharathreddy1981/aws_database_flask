
from AWS import aws_get,aws_get_find,aws_range,aws_post,aws_between
from flask import Flask,jsonify,request

main= Flask(__name__)

@main.route("/test",methods=['GET'])
def add():
    z=aws_get.salt()
    return jsonify(z)

@main.route("/paste/<int:number>",methods=['GET'])
def sub(number):
    z=aws_get_find.bat(number)
    return jsonify(z)

@main.route("/apple/<id>",  methods=["GET"])
def wicket(id):
    phone=aws_range.powder(id)
    return jsonify(phone)


@main.route("/card/<int:id>", methods=['POST'])
def square(id):
    jsondata=request.get_json()
    final=aws_post.bus(jsondata, id)
    return jsonify(final)

@main.route("/mango/<id>/<data>",  methods=["GET"])
def umpire(id,data):
    phone=aws_between.mirchi(id,data)
    return jsonify(phone)


if(__name__=="__main__"):
  main.run(debug=True)

