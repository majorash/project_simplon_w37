# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:14:20 2019
@author: melod
"""

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient


ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"

training_key = ""customvision.py #training_key
prediction_key = "" #prediction_key
prediction_resource_id = "" #prediction_resource_id


publish_iteration_name = "Iteration1"


trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

project =  #projetcid

def classify_photo(url):

    with open(url, "rb") as image_contents:
        #print(url)
        results = predictor.classify_image(
            project.id, publish_iteration_name, image_contents.read())
    
        # Display the results.
        return results.predictions[0].tag_name
    
