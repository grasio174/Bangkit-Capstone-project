from flask import Flask, jsonify, request
from src.database_app import *
import os
from src.load_model import predict
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# set folder upload and rules 
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# routes application API
@app.route('/')
def teman_bagaya():
    return jsonify({'code':'200','message': 'API - TEMAN BAGAYA'})

@app.route('/fashion/catalog')
def catalog():

    # set parameter category & name
    category_arg = request.args.get('category')
    name_arg = request.args.get('name')

    # Filter category and return result item 
    if (category_arg is None or category_arg == '') and (name_arg is None or name_arg == ''):
        items = get_all_items()
        return jsonify(items)
    elif category_arg in ['atasan', 'celana', 'alaskaki']:
        key = 'category'
        value = category_arg
        items = get_items_by_key_value(key, value)
        return  jsonify(items)
    elif name_arg != '':
        key = 'name'
        value = name_arg
        item = get_items_by_key_value(key, value)
        return jsonify(item)
    else:
        return jsonify({'code':'404','message': ' Item - Tidak Ditemukan'})

@app.route('/fashion/predict', methods=['POST'])
def upload():
    # Check if the request contains a file
    if 'file' not in request.files:
        return 'No file found', 400

    file = request.files['file']

    # Check if a file is selected
    if file.filename == '':
        return 'No file selected', 400

    # Check if the file extension is allowed
    if not allowed_file(file.filename):
        return 'Invalid file format', 400

    # Save the file to a specific location
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Call your machine learning model to make predictions using the file
    result_predict = predict(file_path)

    # Remove the uploaded file
    os.remove(file_path)
    
    # get item from catalog 
    value = str(result_predict)
    result_item = get_items_by_key_value('name', value)

    return jsonify(result_item)

@app.errorhandler(404)
def handle_invalid_route(e):
    return 'Invalid API Request', 404

if __name__ == '__main__':
    app.run()
