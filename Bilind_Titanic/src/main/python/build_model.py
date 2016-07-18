import numpy as np
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import KFold, cross_val_score
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

        rf = RandomForestClassifier()
        rf.fit(  x,  y  )
        cv = KFold(len(y))
        rfScore = cross_val_score(rf,x,y,cv=cv,verbose=True,n_jobs=-1)
        print rfScore.mean()

        modelName = Helper().generateFileName( Constant.FILE_PREFIX, name = "model" )

        path = "{}/{}.pkl".format( Constant.MODEL_PATH, modelName )
        joblib.dump( rf, path ) 

        end = time.time()    
        print ('Total time taken for job (sec) = ', end - start)


BuildModel().saveModel()
