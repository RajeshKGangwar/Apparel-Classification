from wsgiref import simple_server
from flask import Flask, render_template,request, jsonify, request, Response
import os
from flask_cors import CORS, cross_origin
from Image_preprocessing.Decoding import DecodeImage
from Image_preprocessing.Encoding import EncodeImage
from prediction.FashionPredict import FashionClassification


app = Flask(__name__)


class main:
    def __init__(self):
        self.model = FashionClassification()



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        image = request.json['image']
        #decoding the image to base64
        DecodeImage(image,"Input_image.jpg")
        result = cliApp.model.FashionPredict("Input_image.jpg")

    except ValueError as val:
        #print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        #print(e)
        result = "Invalid input"
    #print("this is my result", result)

    output = list(result.keys())[list(result.values()).index(1)]
    print("this is the output", output)

    return output





if __name__ == "__main__":
    cliApp = main()
    host = '0.0.0.0'
    port = 5000
    httpd = simple_server.make_server(host,port,app)
    print("Serving on %s %d" % (host, port))
    httpd.serve_forever()



