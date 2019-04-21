import base64
import datetime
import random
from io import BytesIO
from GeneraterImage import GenerateImage
from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
from PIL import Image
import pandas as pd
import tensorflow as tf
import keras
from keras.models import load_model

# configuration
DEBUG = True
PRODUCTION = False

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# to use it when loading the model
def auc(y_true, y_pred):
	auc = tf.metrics.auc(y_true, y_pred)[1]
	keras.backend.get_session().run(tf.local_variables_initializer())
	return auc

# load the model, and pass in the custom metric function
global graph, model
graph = tf.get_default_graph()
model = load_model('model.h5', custom_objects={'auc': auc})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/api', methods=['GET', 'POST'])
def api_version():
	return jsonify(name="SawandeeTukwan",
				   version="1.0.0")

@app.route('/api/randomImage', methods=['GET'])
def randomImage():
	day = datetime.datetime.today().weekday() + 1
	if (day == 7):
		day = 0

	size = request.args.get('size')
	encode = request.args.get('encode') if request.args.get('encode') else 'jpeg'
	url = "https://loremflickr.com/%s/%s/flower" % (size, size)
	image_obj = GenerateImage(url, size, day)
	image_obj.addText()
	image_de = serveImage(image_obj.img, encode)
	return jsonify(base64=base64.b64encode(image_de).decode('utf-8'),
				   type=encode,
				   size=[size, size])

@app.route('/api/customImage', methods=['GET'])
def customImage():
	day = datetime.datetime.today().weekday() + 1
	if (day == 7):
		day = 0

	msg = request.args.get('msg')
	size = request.args.get('size')
	encode = request.args.get('encode') if request.args.get('encode') else 'jpeg'
	url = "https://loremflickr.com/%s/%s/flower" % (size, size)
	image_obj = GenerateImage(url, size, day)
	image_obj.addText(msg)
	image_de = serveImage(image_obj.img, encode)
	return jsonify(base64=base64.b64encode(image_de).decode('utf-8'),
				   type=encode,
				   size=[size, size])

@app.route("/api/predictImage", methods=["GET","POST"])
def predict():
	size = request.args.get('size')
	label_arr = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
	img = GenerateImage("https://loremflickr.com/%s/%s/flower" % (size, size), size)
	data = img.img.getdata()
	data = np.array(data).reshape(-1, 500, 500, 3)
	result = model.predict(data.reshape(-1, 500, 500, 3))
	#result_class = label_arr[np.argmax(result)]
	img.setDay(np.argmax(result))
	img.addText()
	return jsonify(base64=base64.b64encode(image_de).decode('utf-8'),
				   type=encode,
				   size=[size, size])

@app.route("/api/getRandomText", methods=["GET", "POST"])
def getText():
	datasetpath = "../csv/" + str(random.randint(0, 7)) + ".csv"
    with open(datasetpath, encoding="utf-8") as f:
        reader = csv.reader(f)
        low_text = choice(list(reader)) if not msg else msg
    low_text = ''.join(low_text)
    return jsonify(low_text)

def serveImage(image, encode):
    img_io = BytesIO()
    image.save(img_io, encode)
    img_io.seek(0)
    return img_io.getvalue()

if __name__ == '__main__':
    app.run()
