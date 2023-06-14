import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

PATH = './service/service_acc.json'
URL = 'https://temanbagaya-default-rtdb.asia-southeast1.firebasedatabase.app'

def get_all_items():
    # Initialize the Firebase Admin SDK
    cred = credentials.Certificate(PATH)
    firebase_admin.initialize_app(cred, {
        'databaseURL': URL
    })

    # Reference the database location where the data is stored
    ref = db.reference('item/')

    try:
        # Retrieve all items from the database
        result = ref.get()
    except Exception as e:
        # Handle the exception/error
        print("An error occurred:", str(e))
        result = '{"message":"item not exist"}'

    # Close the Firebase Admin SDK
    firebase_admin.delete_app(firebase_admin.get_app())
    return result

def get_items_by_key_value(key, value):
    # Initialize the Firebase Admin SDK
    cred = credentials.Certificate(PATH)
    firebase_admin.initialize_app(cred, {
        'databaseURL': URL
    })

    # Reference the database location where the data is stored
    ref = db.reference('/item')

    # Query the database based on the key-value pair
    try:
        query = ref.order_by_child(key).equal_to(value)
        result = query.get()
    except Exception as e:
        print("An error occurred:", str(e))
        result = '{"message":"item not exist"}'

    # Close the Firebase Admin SDK
    firebase_admin.delete_app(firebase_admin.get_app())
    return result


