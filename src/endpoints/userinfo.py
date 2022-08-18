from fastapi import APIRouter
from fastapi import Query
from fastapi import FastAPI, Response, status,HTTPException
from src.models.userinfo import UserInfoModel
from typing import Optional
import requests
import json

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
    return {"usuarios": response.json() }

@router.get("/{idUsuario}")
async def read_user(idUsuario: str):
    url = 'https://62fd8a326e617f88deab3075.mockapi.io/infoUsers/infoUsers/'+idUsuario
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
    if(response.status_code==  404):
     raise HTTPException(status_code=204, detail="Item not found")
    jsonresponse = json.loads(response.text)
    return jsonresponse


@router.put("/update")
async def read_user(user: UserInfoModel):
    url = 'https://62fd8a326e617f88deab3075.mockapi.io/infoUsers/infoUsers/'
    params = {'UserInfoModel':user}
    response = requests.put(url, params = params, timeout=5)
    if(response.status_code==  404):
     raise HTTPException(status_code=204, detail="Item not found")
    jsonresponse = json.loads(response.text)
    return jsonresponse


@router.delete("/delete/{idUsuario}")
async def read_user(idUsuario: str):
    url = 'https://62fd8a326e617f88deab3075.mockapi.io/infoUsers/infoUsers/'+idUsuario
    response = requests.delete(url)
    if(response.status_code==  404):
     raise HTTPException(status_code=204, detail="Item not found")
    jsonresponse = json.loads(response.text)
    return jsonresponse