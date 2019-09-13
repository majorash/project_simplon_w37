# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:14:20 2019

@author: melod
"""

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient


#----------- Statics (Custom Vision Project access)----------------
ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"

training_key = "<Replace with training key>"
prediction_key = "<Replace with prediction key>"
prediction_resource_id = "<Replace with prediction ressource id>"

publish_iteration_name = "Iteration1"


trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

project = trainer.get_project('<Replace with project id>') #

#-------------------------------------

#----------Function to use in the app--------------------    
def classify_photo(url):

    with open(url, "rb") as image_contents:
        #print(url)
        results = predictor.classify_image(
            project.id, publish_iteration_name, image_contents.read())
    
        # Display the results.
        for prediction in results.predictions:
            print("\t" + prediction.tag_name +
                  ": {0:.2f}%".format(prediction.probability * 100))
        return results.predictions[0].tag_name
    

### Exemple 
#r = classify_photo(r'C:\Projet\PhotoClassifier\data\Photos\animal\IMG_20180510_112719_1.jpg')
#print(r)
            
            
    