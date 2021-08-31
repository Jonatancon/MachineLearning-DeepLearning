#Importar las librerias

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar el data set

dataset = pd.read_csv("Restaurant_Reviews.tsv", delimiter = "\t", quoting = 3)

#Limpieza de texto

import re
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][0])
review = review.lower()
review = review.split()
ps = PorterStemmer()
review = [ps.stem(word) for word in review 
          if not word in set(stopwords.words('english'))]
review = ' '.join(review)
