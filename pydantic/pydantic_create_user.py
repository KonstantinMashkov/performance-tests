import uuid
from datetime import date
from pydantic import BaseModel, Field, HttpUrl, EmailStr, ValidationError

"""
UserSchema
{
  "id": "string",
  "email": "user@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

CreateUserRequestSchema
{
  "email": "user@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

CreateUserResponseSchema
{
  "user": {
    "id": "string",
    "email": "user@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
  }
}
"""

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    last_name: str  = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

class CreateUserResponseSchema(BaseModel):
    user: UserSchema
