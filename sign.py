from signver.detector import Detector
from signver.cleaner import Cleaner
from signver.extractor import MetricExtractor
from signver.matcher import Matcher
from signver.utils import data_utils, visualization_utils
from signver.utils.data_utils import invert_img, resnet_preprocess
from signver.utils.visualization_utils import plot_np_array, visualize_boxes, get_image_crops, make_square
from skimage.color import rgb2gray


import numpy as np
import tensorflow as tf
import matplotlib
import matplotlib.pyplot as plt

detector_model_path = "models/detector/small" #Detector
detector = Detector()
detector.load(detector_model_path)

extractor_model_path = "models/extractor/metric" #Extractor
extractor = MetricExtractor() 
extractor.load(extractor_model_path)

cleaner_model_path = "models/cleaner/small" #Cleaner
cleaner = Cleaner() 
cleaner.load(cleaner_model_path)

matcher = Matcher()

"""
# Further code run as function(OPTION 1)
"""

import cv2
from numpy import asarray

def signv(img_p1,img_p2):
 
  img_arr1=data_utils.img_to_np_array(img_p1) 
  img_arr2=data_utils.img_to_np_array(img_p2)
  signatures=[]
  signatures.append(img_arr1)
  signatures.append(img_arr2)
  sigs= [ resnet_preprocess( x, resnet=False ) for x in signatures ]
  norm_sigs = [ x * (1./255) for x in sigs]
  cleaned_sigs = cleaner.clean(np.array(norm_sigs))
  cleaned_feats = extractor.extract(cleaned_sigs ) 
  c_feat1,c_feat2= cleaned_feats[0,:], cleaned_feats[1,:]
  if matcher.cosine_distance(c_feat1,c_feat2)>0.2:
    return "not verified"
  else:
    return "verified"

# print(signv(r"F:\BOB\sign_directory\630801551452.jpeg",r"F:\BOB\sign_directory\630801551452.jpeg")) #1-pick from database, 2- take from api















