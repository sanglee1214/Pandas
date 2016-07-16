import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from patsy import dmatrices
from sklearn.cross_validation import train_test_split, cross_val_score
from sqlalchemy import create_engine
import csv
import os
import time

from constant import Constant
from helper import Helper

class PrepareData():

    def __init__(self):

        serverUser = os.environ.get( "SERVER_USER" )
        serverPassword = os.environ.get( "SERVER_PASSWORD" )
        serverHost = os.environ.get( "SERVER_HOST" )
        dbName = os.environ.get( "SERVER_DB_NAME" )
        tableName = os.environ.get( "TABLE_NAME" )
        testPercent = os.environ.get( "TEST_PERCENT", 0.30 )

        self.connectStr = "postgresql://{}:{}@{}/{}".format(
            serverUser,
            serverPassword,
            serverHost,
            dbName
        )

        self.query = '''SELECT 
                            "PassengerId", 
                            "Survived", 
                            "Pclass", 
                            "Fare", 
                            "Sex", 
                            "Age"
                        FROM {} 
                        WHERE "Age" != %s
                    '''.format( tableName )

        self.testPercent = float( testPercent )

    def loadPipeline(self):
        start = time.time()

        df = self.callQuery()
        finalDf = self.createDummies(df)

        y = finalDf.Survived
        x = finalDf[ finalDf.columns[1:] ]

        xTrain, xTest, yTrain, yTest = train_test_split( 
            x, y, test_size = self.testPercent, random_state = 42 
        )

        xTrain["Survived"] = yTrain
        xTest["Survived"] = yTest

        print xTrain.head()

        self.saveFiles(xTest,xTrain)

        end = time.time()
        print ('Total time taken for job (sec) = ', end - start)

    def callQuery(self):
        engine = create_engine( self.connectStr )
    	df = pd.read_sql( self.query, engine, params = [np.nan] )
        return df

    def createDummies(self, df):
        df["AgeGroup"] = df.Age.apply(self.binAge)
        df["Sex"] = df.Sex.apply(self.sexToInt)

        otherPreds = df.columns[1:4]

        dummiesAgeGrp = pd.get_dummies( df.AgeGroup, prefix = "AgeGroup" )
        dummiesSex = pd.get_dummies( df.Sex, prefix = "Sex" )

        join1 = df[otherPreds].join(dummiesAgeGrp)
        join2 = join1[ join1.columns[:7] ].join(dummiesSex)

        finalDf = join2[ join2.columns[:8] ]

        return finalDf

    def binAge(self,age):
        if( age >=  Constant.AGE_GROUP_5_THRESHOLD ):
            return Constant.AGE_GROUP_5
        elif ( age >= Constant.AGE_GROUP_4_THRESHOLD ):
            return Constant.AGE_GROUP_4
        elif ( age >= Constant.AGE_GROUP_3_THRESHOLD ):
            return Constant.AGE_GROUP_3
        elif ( age >= Constant.AGE_GROUP_2_THRESHOLD ):
            return Constant.AGE_GROUP_2

        return Constant.AGE_GROUP_1

    def sexToInt(self,sex):
        if( sex == Constant.MALE ):
            return Constant.MALE_INT
        return Constant.FEMALE_INT         

    def saveFiles(self,testDf,trainDf):

        fileNameTest = Helper().generateFileName( Constant.FILE_PREFIX, name = "test" )
        fileNameTrain = Helper().generateFileName( Constant.FILE_PREFIX, name = "train" )

        fileTestPath = "{}/{}.csv".format( Constant.PATH, fileNameTest )
        fileTrainPath = "{}/{}.csv".format( Constant.PATH, fileNameTrain )

        testDf.to_csv( path_or_buf = fileTestPath, sep=',', index = False  )
        trainDf.to_csv( path_or_buf = fileTrainPath, sep=',', index = False )

        print "Successfuly Saved Files to Path {}".format( Constant.PATH )


pipeLineObj =  PrepareData()
pipeLineObj.loadPipeline()