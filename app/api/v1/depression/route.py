from fastapi import APIRouter
from .schema import DepressionRequest
from .service import get_depression

router = APIRouter()

@router.post('/depression', tags=['Depression'])
def assess_depression(data: DepressionRequest):
    return  get_depression()