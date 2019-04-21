import base64
import datetime
from io import BytesIO
from GeneraterImage import GenerateImage
from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True
PRODUCTION = False

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

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


def serveImage(image, encode):
    img_io = BytesIO()
    image.save(img_io, encode)
    img_io.seek(0)
    return img_io.getvalue()

if __name__ == '__main__':
    app.run()