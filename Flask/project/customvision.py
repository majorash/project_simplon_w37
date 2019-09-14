from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient


ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"

training_key = "22ef4a89c10b4e0d8d6cdaabce6b7221"
prediction_key = "467bd9a7c49a41f49a9cbf6846379e32"
prediction_resource_id = "/subscriptions/f08d91e4-8ee9-45bb-b518-f36e0aecb653/resourceGroups/Castelnau/providers/Microsoft.CognitiveServices/accounts/Classifier_GroupProject_Prediction"


publish_iteration_name = "Iteration1"


trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

project = trainer.get_project('365bd7c3-f643-47c0-a0d3-91f7fb50a65a')

def classify_photo(url):

    with open(url, "rb") as image_contents:
        #print(url)
        results = predictor.classify_image(
            project.id, publish_iteration_name, image_contents.read())
    
        # Display the results.
        return results.predictions[0].tag_name
    