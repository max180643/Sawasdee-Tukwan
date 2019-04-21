import base64
from io import BytesIO, StringIO
from GeneraterImage import GenerateImage
from flask import Flask, jsonify, request, send_file
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
	size = request.args.get('size')
	encode = request.args.get('encode') if request.args.get('encode') else 'jpeg' 
	url = "https://picsum.photos/%s/%s?random=1" % (size, size)
	image_obj = GenerateImage(url, size)
	image_obj.addText()
	image_de = serveImage(image_obj.img, encode)
	#image_bstr = image_de.read()
	#image_str = image_bstr.encode('UTF-8')
	#image_ = ("<img src='data:image/%s;base64," % encode) + base64.b64encode(image_de).decode('utf-8') + "'/>" 

	return jsonify(base64=base64.b64encode(image_de).decode('utf-8'),
				   type=encode,
				   size=[size, size])

@app.route('/api/customImage', methods=['GET'])
def customImage():
	msg = request.args.get('msg')
	size = request.args.get('size')
	encode = request.args.get('encode') if request.args.get('encode') else 'jpeg' 
	url = "https://loremflickr.com/%s/%s/flower" % (size, size)
	image_obj = GenerateImage(url, size)
	image_obj.addText(msg)
	image_de = serveImage(image_obj.img, encode)
	#image_bstr = image_de.read()
	#image_str = image_bstr.encode('UTF-8')
	#image_ = ("<img src='data:image/%s;base64," % encode) + base64.b64encode(image_de).decode('utf-8') + "'/>" 

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