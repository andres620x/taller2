from pydantic import BaseModel, Field
from typing import Optional

class UserInfoModel(BaseModel):
    idUsuario: Optional[str] = ''
    internalId:  Optional[str] = ''