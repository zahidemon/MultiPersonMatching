from scipy.constants.codata import precision

import pose_match
import parse_openpose_json
import numpy as np
import logging
import prepocessing
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
json_data_path = 'data/json_data/'
images_data_path = 'data/image_data/'

'''
-------------------- MULTI PERSON -------------------------------------
'''
model = "duo3"
input = "duo4"
model_json = json_data_path + model + '.json'
input_json = json_data_path + input + '.json'
model_image = images_data_path + model + '.jpg'
input_image = images_data_path + input + '.jpg'

model_features = parse_openpose_json.parse_JSON_multi_person(model_json)
input_features = parse_openpose_json.parse_JSON_multi_person(input_json)

'''
model1 = model_features[0]
models_array = [np.array(model1)]
model2 = model_features[1]
models_array = [np.array(model1), np.array(model2)]
'''

models_array = model_features

#Simple case; poses are not checked on relation in space
pose_match.multi_person(models_array, input_features, model_image, input_image)

#Second case; poses ARE checked on relation in space
#pose_match.multi_person2(models_array, input_features, model_image, input_image)

'''
-------------------------------- SINGLE PERSON -------------------------------------------
Read openpose output and parse body-joint points into an 2D array of 18 rows
Elke entry is een coordinatenkoppel(joint-point) in 3D , z-coordinaat wordt nul gekozen want we werken in 2D
'''

model = "foto1"
input = "midget1"
model_json = json_data_path + model + '.json'
input_json = json_data_path + input + '.json'

model_image = images_data_path + model + '.jpg'
input_image = images_data_path + input + '.jpg'

model_features = parse_openpose_json.parse_JSON_single_person(model_json)
input_features = parse_openpose_json.parse_JSON_single_person(input_json)

input_features = prepocessing.unpad(input_features)
model_features = prepocessing.unpad(model_features)


'''
Calculate match fo real (incl. normalizing)
'''
#(result, error_score, input_transform) = pose_match.single_person(model_features, input_features, True)
#logger.info("--Match or not: %s ", str(result))

'''
Calculate match + plot the whole thing
'''
#pose_match.plot_single_person(model_features, input_features, model_image, input_image)



