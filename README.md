# Teman Bagaya
## Cloud Comptuing 

we are develop private API for our application, to get item from database and get item from model predict  <br>

## About Our API 

We have developed our API using Python and the Flask framework. For storing static data such as images, we utilize Google Storage buckets. Our data catalog is stored in Firebase Realtime Database. To deploy our API, we leverage Cloud Run. <br>
  
## Build the API 

to build this API we need to install requirements.txt for get depedency for our API 
```
pip install -r requirements.txt 
```
After installing all the dependencies, the next step is to download the machine learning model and obtain the service account for accessing the realtime-database from Firestore. Therefore, we need to create a folder to store the service account and the model file. Once all the necessary dependencies are available, we can try running this API on a local machine using the following command: 
```
gunicorn -b 8000 server:app 
```
And we can try some features from this API using curl 
```
# get all data catalog from database 
curl -X GET localhost:8000/fashion/catalog

# get data catalog by category atasan from database 
curl -X GET localhost:8000/fashion/catalog?category=atasan

# get data catalog by name item from database 
curl -X GET localhost:8000/fashion/catalog?name=Kaos Oversized

# get data predict from Machine Learning model 
curl -X POST -f "file=@name_image.jpg" localhost:8000/fashion/predict 
```
category just have 3 choice it's atasan, celana, and alaskaki. 

## Deploy API 

