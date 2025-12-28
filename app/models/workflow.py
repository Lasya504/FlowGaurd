from pydantic import BaseModel
from typing import List

class Workflow(BaseModel):
    workflow_name: str
    steps: List[str]
