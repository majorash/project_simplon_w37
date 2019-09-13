# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:25:42 2019
     Access to the group project classificator with CustomVision
@author: melody
"""

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

class CustomVisionAPI(object):
    
    def __init__(self, training_key='',
                 prediction_key='',
                 prediction_resource_id='',
                 project_id=''):
        
        self.ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"

        self.training_key = training_key #"<Replace with training key>"
        self.prediction_key = prediction_key #"<Replace with prediction key>"
        self.prediction_resource_id = prediction_resource_id #"<Replace with prediction ressource id>"

        self.publish_iteration_name = "Iteration1"


        self.trainer = CustomVisionTrainingClient(training_key, endpoint=self.ENDPOINT)
        self.predictor = CustomVisionPredictionClient(prediction_key, endpoint=self.ENDPOINT)

        self.project = self.trainer.get_project(project_id) #'<Replace with project id>'
            

    def classify_photo(self,url):

        with open(url, "rb") as image_contents:
            #print(url)
            results = self.predictor.classify_image(
                self.project.id, self.publish_iteration_name, image_contents.read())
        
            # Display the results.
            for prediction in results.predictions:
                print("\t" + prediction.tag_name +
                      ": {0:.2f}%".format(prediction.probability * 100))
        return results.predictions[0].tag_name



# Exemple
#CustomVisionAPI().classify_photo(r'C:\Projet\PhotoClassifier\data\Photos\animal\IMG_20180510_112719_1.jpg')