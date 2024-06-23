import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient
import numpy as np
# from sklearn.model_selection import GridSearchCV
# from sklearn.metrics import r2_score
import pymysql

# import pickle
# import numpy as np 
url=os.getenv("MONGO_DB_URL") 
db=os.getenv("db_name")
coll=os.getenv("collection_name")
load_dotenv()


def export_collection_as_dataframe(url,coll, db):
    try:
        logging.info("started connecting",)
        
        mongo_client = MongoClient(url)
        collection = mongo_client[db][coll]
        df = pd.DataFrame(list(collection.find()))
        
        if "_id" in df.columns.to_list():
            df = df.drop(columns=["_id"], axis=1)

        df.replace({"na": np.nan}, inplace=True)
        logging.info("connection established",)
        print(df.head())
        return df
    
    except Exception as e:
        raise CustomException(e, sys)




# def save_object(file_path, obj):
#     try:
#         dir_path = os.path.dirname(file_path)

#         os.makedirs(dir_path, exist_ok=True)

#         with open(file_path, "wb") as file_obj:
#             pickle.dump(obj, file_obj)

#     except Exception as e:
#         raise CustomException(e, sys)

# def evaluate_models(X_train, y_train,X_test,y_test,models,param):
#     try:
#         report = {}

#         for i in range(len(list(models))):
#             model = list(models.values())[i]
#             para=param[list(models.keys())[i]]

#             gs = GridSearchCV(model,para,cv=3)
#             gs.fit(X_train,y_train)

#             model.set_params(**gs.best_params_)
#             model.fit(X_train,y_train)

#             #model.fit(X_train, y_train)  # Train model

#             y_train_pred = model.predict(X_train)

#             y_test_pred = model.predict(X_test)

#             train_model_score = r2_score(y_train, y_train_pred)

#             test_model_score = r2_score(y_test, y_test_pred)

#             report[list(models.keys())[i]] = test_model_score

#         return report

#     except Exception as e:
#         raise CustomException(e, sys)
