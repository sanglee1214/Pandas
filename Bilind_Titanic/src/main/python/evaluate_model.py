import numpy as np
import pandas as pd 
import csv
import os
import time
from sklearn import metrics
from sklearn.externals import joblib

from constant import Constant
from helper import Helper

class EvaluateModel():

    def getPredictions(self):
        start = time.time()

        fileNameTest = os.environ.get( "FILE_NAME_TEST" )
        modelName = os.environ.get( "MODEL_NAME" )

        modelPath = "{}/{}".format( Constant.MODEL_PATH, modelName )
        model = joblib.load(modelPath) 

        dfTest = pd.read_csv( "{}/{}".format(Constant.PATH,fileNameTest), sep = "," )
        testColumns = dfTest.columns

        x = dfTest[ testColumns[:7] ]
        y = dfTest.Survived

        dfTest["predictedProb"] = model.predict(x)
        predicted = dfTest.predictedProb
        #dfTest["predictedClass"] = model.predict_proba(X)

        coefDf = pd.DataFrame(list(zip(x.columns, np.transpose(model.coef_))))

        print coefDf
        print metrics.accuracy_score(y, predicted)
        print metrics.classification_report(y, predicted)
        print metrics.confusion_matrix(y, predicted)

        end = time.time()    
        print ('Total time taken for job (sec) = ', end - start)

EvaluateModel().getPredictions()
