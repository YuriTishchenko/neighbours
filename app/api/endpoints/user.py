from fastapi import APIRouter



router = APIRouter()

@router.get(
    '/',
)
async def get_all_users():
    pass

@router.patch(
    '/{user_id',
)
async def partially_update_user(
        user_id: int,
):
    """Только для супер юзеров"""
    pass

@router.delete(
    '/{user_id}',
)
async def remove_user_id(
        user_id: int,
)
    pass

