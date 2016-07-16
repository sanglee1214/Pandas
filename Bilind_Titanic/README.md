# titanic

Requirements: Python 2.7, Anaconda with following python libraries installed (pip install dependency_name)

1. numpy
2. pandas
3. sklearn
4. csv
5. time
6. pickle

This app represents a series of pipelines. The app is made to ensure consistency in model building for a titanic dataset. The model will give likelihood of surviving the titanic, given a passengers, Pclass, Fare, Sex and AgeGroup, and there corresponding label (survived wreck or not). 

Pipeline 1. prepare_data.sh

Creates a member of PrepareData() class and calls object method perform. Which will query a remote postgres database, and transform the data for model building purposes, and will save 2 sets of csv files. A train file set, and a test file set. Note when these files are read, they are ready for model building (no null values, category binning/dummy variable creation implemented, n - 1 dummy variables in final dataframes). 

prepare_data.sh requires four parameters that the user must enter when running the bash script, SERVER_USER, SERVER_PASSWORD, SERVER_HOST and SERVER_DB name. 

example, from the root directory of the app. 

sh ./prepare_data.sh server_user server_password server_host server_db table_name test_percent

1. server_user = username for machine
2. server_password = password for machine
3. server_host = machine name
4. server_db = database name
5. table_name = database table name holding titanic dataset
6. test_precent = % of data to be randomly split for test data (default is 30% if no value entered)

The test and train csv files will be saved in ./src/main/assets. Any file will always have a unique name (by attaching timestamp to file name in Helper.generateFileName( params ). So prepare_data.sh can be run multiple times without having to delete files. 

Pipeline 2. build_model.sh

Creates a member of BuildModel() class and calls object method saveModel(). In saveModel(), the trainData set (generated from PrepareData().loadPipeline, is read as pandas dataframe, and a logistic regression model is built, and then saved to ./src/main/models as a series of 5 .plk files. Note all these files must be present, when importing the model in another process (In EvaluateModel().getPredictions). 

build_model.sh requires 1 parameter that the user must enter when running the bash script, FILE_NAME_TRAIN, which is the name of the csv file in assets represeting the train data set. 

example. from the root directory of the app/ 

sh ./build_model.sh titanic_train_07:10:16:22:32:08.csv

Pipeline 3. evaluate_model.sh

Creates a member of the EvaluateModel() class, and calls the object method getPredictions. in getPredictions, the testData set (generated from PrepareData().loadPipeline), is read as a pandas dataframe, and the logistic regression model (also built from PrepareData().loadPipeline) is imported, and this imported model is used to get predictions form this test dataset. The coefficients of the logistic regression model, accuracy score, and classification report are also outputted when script is run. 

evaluate_model.sh requires 2 parameters that the user must enter when running the bash script, FILE_NAME_TEST, which is the name of the csv file in assets represeting the test data set, and model name (name of logit model saved during build_model.sh. 

example, from the root directory of the app/ 

sh ./evaluate_model.sh titanic_test_07:10:16:22:32:08.csv titanic_model_07:10:16:22:50:21.pkl

The entire pipeline is below, and should be run in this order as well. 

1. sh ./prepare_data.sh server_username server_password server_host database_name

2. sh ./build_model.sh train_data_set_name.csv

3. sh ./evaluate_model.sh test_data_set_name.csv pipeline_model_name.pkl
