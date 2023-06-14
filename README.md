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
after install all depedency, we need to download the model machine learning, service account for access realtime-database from firestore, so we need make the folder for service account and model for that item.
And after the all depedency needed avaible we can
try to run this API on local machine with this command 
```
gunicorn -b 8000 server:app 
```
And we can try using some features from this API like 
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


