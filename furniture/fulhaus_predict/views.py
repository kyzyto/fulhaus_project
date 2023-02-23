from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import requests
from django.http import JsonResponse


@csrf_exempt
def predict_image(request):
    # Get the image file from the POST request
    image_file = request.FILES['image']

    if image_file is not None:
        # Set the URL and headers for the remote server
        url = 'https://predict.app.landing.ai/inference/v1/predict?endpoint_id=275c6d4d-93cf-4d56-a52c-1e9bae06cc3c'

        headers = {
            'apikey': '8rk01n3ndxh8qqivnodnohnm2857rh9',
            'apisecret': 'd6vopbnf201tdywwx1nz5bwldh17q8jwwyxipo52f9syfbeswopednd5s52glc'
        }

        # Send the POST request to the remote server
        files = {'file': image_file}
        response = requests.post(url, headers=headers, files=files)

        # Return the JSON response from the remote server to Postman
        return JsonResponse(response.json())
    else:
        # Return an error message if the 'image' key is not found
        return JsonResponse({'error': 'Image file not found in request.'})
