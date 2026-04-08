from pydantic import BaseModel, ConfigDict

class ServiceCreate(BaseModel):
    name: str
    url: str

class ServiceResponse(BaseModel):
    id: int
    name: str
    url: str
    status: str

    model_config = ConfigDict(from_attributes=True)