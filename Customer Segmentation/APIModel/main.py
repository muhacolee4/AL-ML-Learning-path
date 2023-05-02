import pandas as pd
import numpy as np
from fastapi import FastAPI
import pickle
from models import Customer
from sklearn.preprocessing import MinMaxScaler

dfo = pd.read_csv("df.csv")
#dfo = dfo.drop("Unnamed: 0", axis='columns')

with open("/Users/coura/OneDrive/Desktop/Customer Segmentation/APIModel/model_pickle", "rb") as f:
    mb = pickle.load(f)
app = FastAPI()

scaler = MinMaxScaler()

scaled = scaler.fit_transform(dfo)
scaledDF = pd.DataFrame(scaled, columns=dfo.columns)

@app.get("/")
def greetings():
    return "Hello World"

@app.post("/predict_cluster")
def cluster(customer:Customer):
    try:
        customer = customer.dict()
        df = pd.DataFrame(customer, index=[0])

        df['housing']=df['housing'].map({'no':0,'yes':1})
        df['loan']=df['loan'].map({'no':0,'yes':1})
        df['subscribed']=df['subscribed'].map({'no':0,'yes':1})

        # categorized the jobs
        df['job'] = df['job'].replace(['housemaid','unemployed','unknown','student'],'tier1')
        df['job']= df['job'].replace(['services','technician','retired'],'tier2')
        df['job']=df['job'].replace(['admin','blue-collar','management','self-employed','entrepreneur'],'tier3')

        df['education']=df['education'].replace(['illiterate','basic.4y', 'high.school', 'basic.6y', 'basic.9y','unknown'],'non-educated')
        df['education']=df['education'].replace(['university.degree','professional.course'],'educated')

        processedDf = pd.get_dummies(df, columns=['job','education','marital','default','poutcome'])
        missing_cols = set(dfo.columns) - set(processedDf.columns)
        for col in missing_cols:
            processedDf[col] = 0
        processedDf = processedDf.reindex(columns=dfo.columns[:], fill_value=0)
    #
        processedDf = processedDf.replace(to_replace={True : 1, False:0})
        scaledExample = scaler.transform(processedDf)
        scaledExampleDF = pd.DataFrame(scaledExample, columns=processedDf.columns)
    #
        cluster = mb.predict(scaledExampleDF)
        return f"This example belongs to cluster {str(cluster)}"
    except:
        return "Incorrect Values Passed"





