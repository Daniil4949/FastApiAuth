from uuid import UUID
from pydantic import BaseModel, Field, validate_email, validator, EmailStr
from email_validator import validate_email, EmailNotValidError
from fastapi import HTTPException, status


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None


class UserAuth(BaseModel):
    username: str = Field(..., description="username")
    email: EmailStr = Field(..., description="user email")
    password: str = Field(..., min_length=5, max_length=24, description="user password")


class UserOut(BaseModel):
    email: str


class SystemUser(UserOut):
    password: str

# from fastapi import FastAPI, Depends, UploadFile, File, Form, HTTPException, status
# from email_validator import validate_email, EmailNotValidError
# from typing import List, Optional
#
#
# def check_email(email: str):
#     try:
#         validation = validate_email(email, check_deliverability=False)
#         return validation.email
#     except EmailNotValidError as e:
#         raise HTTPException(detail=f"'{email}' is not a valid email address. {str(e)}",
#                             status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
#
#
# def email_checker(emails: List[str] = Form(...)):
#     if len(emails) == 1:
#         emails = [item.strip() for item in emails[0].split(',')]
#
#     return [check_email(email) for email in emails]
