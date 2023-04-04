from fastapi import status, HTTPException, APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth.schemas import UserOut, UserAuth, TokenSchema
from app.db import get_email, add_new_user, get_username
from auth.tokens import get_hashed_password, verify_password, create_access_token, create_refresh_token
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/auth",
    scheme_name="JWT"
)


@router.post("/signup", summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    user_email = get_email(data.email)
    username = get_username(data.username)
    if user_email is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    if username is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exist"
        )
    user = {
        "email": data.email,
        "password": get_hashed_password(data.password),
        "username": data.username
    }
    add_new_user(user)
    return user


@router.post("/login", summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user: dict = get_username(form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This username does not exists"
        )
    hashed_password = user["password"]
    if not verify_password(form_data.password, hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="incorrect email or password"
        )
    return {
        "access_token": create_access_token(user["email"]),
        "refresh_token": create_refresh_token(user["email"])
    }



