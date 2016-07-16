import numpy as np
import pandas as pd 
from sklearn.linear_model import LogisticRegression
import csv
import os
import time

from constant import Constant
from helper import Helper

import pickle
from sklearn.externals import joblib

class BuildModel():

    def saveModel(self):
        start = time.time()

        fileNameTrain = os.environ.get( "FILE_NAME_TRAIN" )

        dfTrain = pd.read_csv( "../assets/{}".format(fileNameTrain), sep = "," )
        trainColumns = dfTrain.columns

        x = dfTrain[ trainColumns[:7] ]
        y = dfTrain.Survived

        logreg = LogisticRegression()
        logreg.fit(  x,  y  )

        print logreg.score( x, y )

        modelName = Helper().generateFileName( Constant.FILE_PREFIX, name = "model" )

        path = "{}/{}.pkl".format( Constant.MODEL_PATH, modelName )
        joblib.dump( logreg, path ) 

        end = time.time()    
        print ('Total time taken for job (sec) = ', end - start)


BuildModel().saveModel()
