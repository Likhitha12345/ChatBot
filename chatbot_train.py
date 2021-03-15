import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import numpy
import keras
from keras.models import Sequential
from keras.layers import Dense,Activation , Dropout
from keras.optimizers import SGD
import random

nltk.download('wordnet')