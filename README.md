# Fulhaus Predict API
This is a Django-based API that allows you to send an image file to a remote server for prediction using a deep learning model. The server can be accessed through a RESTful API that accepts image files via a POST request and returns a prediction in JSON format.


# Steps
1. Install python3
2. Install pip3
3. Install homebrew
4. install django
5. Setup your IDE: Pycharm, VS Code, etc.
6. Run API
7. Testv using ARC
8. Containerize and test.

# Installation
Clone this repository to your local machine, see the document attached seperately via email for the apikey and apisecret and replace the placehold in the "/furniture/furniture/fulhaus_predict/views.py" module.

## Create a virtual environment using a tool such as virtualenv or conda.
## Install the required Python packages using pip install:
1. pip3 install django
2. pip3 install requests

**Run the Django server using the command python manage.py runserver.**

## Usage
To use the API, you can send a POST request to the /fulhaus_predict/predict/ endpoint with the image file as a form data parameter named "image" using an Advanced REST Client such as postman. You can either pass in the image file directly or provide the local file path to the image. Here's an example using curl:


curl -X POST -H "Content-Type: multipart/form-data" -F "image=@/path/to/image.jpg" http://localhost:8000/fulhaus_predict/predict/

The API will return a JSON response containing the predicted label name, like this:
```json
{
    "backbonetype": "ObjectDetectionPrediction",
    "backbonepredictions": {
        "d5e465ba-38f4-4721-9e3e-9ad8f3fe3b53": {
            "score": 0.9244511723518372,
            "defect_id": 55151,
            "coordinates": {
                "xmin": 14,
                "ymin": 67,
                "xmax": 304,
                "ymax": 266
            },
            "labelIndex": 2,
            "labelName": "Bed"
        }
    },
    "predictions": {
        "score": 0.9244511723518372,
        "labelIndex": 1,
        "labelName": "NG"
    },
    "type": "ClassificationPrediction",
    "latency": {
        "preprocess_s": 0.004876136779785156,
        "infer_s": 0.1650092601776123,
        "postprocess_s": 0.00031375885009765625,
        "serialize_s": 0.0025153160095214844,
        "input_conversion_s": 0.001619100570678711,
        "model_loading_s": 0.0002143383026123047
    },
    "model_id": "e8c71020-c6d0-4262-9b0f-54b6436ae695"
}
```
### How to build the Docker
docker build -t furniture .

### How to run the Docker
docker run -p 8001:8000 furniture
