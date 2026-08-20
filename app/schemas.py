#schemas for post creation and validation using pydantic
from pydantic import BaseModel

class postcreate(BaseModel):
    title: str
    content: str
    