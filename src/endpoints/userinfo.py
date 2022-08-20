from fastapi import APIRouter
from fastapi import Query
from fastapi import FastAPI, Response, status,HTTPException
from src.models.userinfo import UserInfoModel
from typing import Optional
import requests
import json


import logging

logger = logging.getLogger(__name__)  # the __name__ resolve to "uicheckapp.services"
                                      # This will load the uicheckapp logger


#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/infoUsers",
    tags=["infoUsers"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_root():
    url = 'https://62fd8a326e617f88deab3075.mockapi.io/infoUsers/infoUsers/'
    response = requests.get(url, {}, timeout=5)
    logger.info("Hola logger usuarios")
    return {"usuarios": response.json() }

@router.get("/{internalId}")
async def read_user(internalId: str):
    url = 'https://62fd8a326e617f88deab3075.mockapi.io/infoUsers/infoUsers/'+internalId
    response = requests.get(url, {}, timeout=5)
    if(response.status_code==  500):
     raise HTTPException(status_code=204, detail="Item not found")
    jsonresponse = json.loads(response.text)
    return jsonresponse


@router.post("/add")
async def add_user(user: UserInfoModel):
    url = 'https://62fd8a326e617f88deab3075.mockapi.io/infoUsers/infoUsers/'
    params = {'UserInfoModel':user}
    response = requests.post(url, params = params, timeout=5)
    jsonresponse = json.loads(response.text)
    return jsonresponse


@router.put("/update/{internalId}")
async def read_user(user: UserInfoModel,internalId: str):
    url = 'https://62fd8a326e617f88deab3075.mockapi.io/infoUsers/infoUsers/'+internalId
    data=json.loads(user.json())
    response = requests.put(url, data = data, timeout=5)
    if(response.status_code==  404):
     raise HTTPException(status_code=204, detail="Item not found")
    jsonresponse = json.loads(response.text)
    return jsonresponse


@router.delete("/delete/{internalId}")
async def read_user(internalId: str):
    url = 'https://62fd8a326e617f88deab3075.mockapi.io/infoUsers/infoUsers/'+internalId
    response = requests.delete(url)
    if(response.status_code==  404):
     raise HTTPException(status_code=204, detail="Item not found")
    jsonresponse = json.loads(response.text)
    return jsonresponse