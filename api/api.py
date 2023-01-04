from fastapi import FastAPI
from schema import CustomerInput
import pickle

api_app = FastAPI(title="Telco Customer Churn API",
                  description="Api para predecir si nuestros clientes se van o se quedan",
                  version="0.1.0")


@api_app.get("/")
async def read_root():
    return {"API": "Telco Customer Churn API v0.1.0"}


@api_app.post("/predict")
async def predict_customer(customer: CustomerInput):
    dv_pickle = pickle.load(open('./models/dv.pkl', 'rb'))
    loaded_model = pickle.load(open('./models/model.pkl', 'rb'))
    cust_dict = customer.dict()
    dv_customer = dv_pickle.transform([cust_dict])
    churn_prob = loaded_model.predict_proba(dv_customer)[0, 1] * 100
    return {"churnProb": churn_prob}
