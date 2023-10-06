"""
Wrapper APIs. 
"""
from fastapi import APIRouter
from pydantic import BaseModel

class CatalogData(BaseModel):
    """
    Pydantic data model for DOME 4.0 catalog datasets.
    """
    Dataset: list
    IssueDate: str
    License: str
    Title: str
    URL: str
    dataCreator: str
    dataPublisher: str
    keyword: str

router = APIRouter()


@router.get("/")
async def home():
    """
    API for testing.
    Return a simple "Hello World" message.

    Returns:
        A dictionary with a message key and "Hello World" value.
    """
    return {"msg": "Hello World from connector service"}


@router.get("/results")
async def search_results(search_string: str):
    """Fill in your way of populating the data and metadata arrays here"""
    metadata: list = []
    data: list = []
    return {"metadata": metadata, "data": data}


@router.get("/results/metadata")
async def search_results_metadata(search_string: str):
    """Fill in your way of populating the metadata here"""
    metadata: list = []
    return metadata

@router.get("/fair")
async def return_fair():
    """This endpoint is used for the FAIR assessment service
       It should return data relevant for the FAIR assessment service of DOME
       This is not known at this point in time
    """
    return str("N/A")
