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

## Deploy Database & static item to Bucket 
Our team stores static data, such as item images from outfits, in a Google Storage bucket. For our database, we use the real-time database provided by Firestore. To deploy our data to Firestore, we follow these steps: 
<br>
1. Collect all the necessary data.<br>
2. Format the data into JSON according to the rules specified in the Firebase documentation.<br>
3. Export the data as "database.json" to the real-time database on Firebase.  <br>

## Deploy API & Mechine Learning to Cloud run 
For deploying our API and machine learning model, we use Cloud Run. Before deployment, we provide the API code, requirements.txt for installing the required dependencies, and the machine learning model. Once everything is available, we create a Dockerfile to build a container image of our API. After the image is ready, we directly deploy it to Cloud Run. Below is the script to deploy our API and machine learning model. 
```
# Build the Docker image locally with the specified tag name
docker build -t teman_bagaya .

# Tag the Docker image with the desired repository path
docker tag teman_bagaya gcr.io/bangkit-capstone-c23-ps012/teman_bagaya

# Push the Docker image to the Google Container Registry (GCR)
docker push gcr.io/bangkit-capstone-c23-ps012/teman_bagaya

# Deploy the Docker image to Cloud Run
gcloud run deploy api --image gcr.io/bangkit-capstone-c23-ps012/teman_bagaya --platform managed --region asia-southeast2

```

## Delploy Website Frontend to App Engine 
For our website, we only use HTML, CSS, and JavaScript. After preparing the website, 
the next step is to deploy it to App Engine. Before deployment, we need to 
prepare the app.yaml file and determine the desired runtime to be used.

```
# app.yaml 
runtime:python39
service: frontend
```
and below is the command to deploy our website to app engine
```
# Deploy Command 
gcloud app deploy 
```
