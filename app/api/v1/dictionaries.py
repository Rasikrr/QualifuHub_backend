from fastapi import APIRouter
from app.models.domain import CategoryEnum

router = APIRouter()

@router.get("/categories")
def get_categories():
    return [category.value for category in CategoryEnum]
