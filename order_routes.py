from fastapi import APIRouter



order_route = APIRouter(
    prefix='/orders',
    tags=['orders']
)


@order_route.get('/')
async def hello():
    return {"message":"Hello"}