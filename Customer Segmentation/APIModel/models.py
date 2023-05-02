from pydantic import BaseModel

class Customer(BaseModel):
    age: int
    job: str
    marital: str
    education: str
    default: str
    housing: str
    loan: str
    campaign: int
    previous: int
    poutcome: str
    subscribed: str