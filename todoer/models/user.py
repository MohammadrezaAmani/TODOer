from pydantic import BaseModel

from todoer.models.base import Base


class UserSignIn(BaseModel):
    email: str
    password: str


class BaseUser(Base):
    email: str
    first_name: str | None = None
    last_name: str | None = None


class UserSignUp(BaseUser):
    password: str
    repeat_password: str

    def __init__(self, **data):
        super().__init__(**data)
        if self.password != self.repeat_password:
            raise ValueError("Passwords do not match")
        self.repeat_password = None

    def model_dump(self, **kwargs):
        d = super().model_dump(**kwargs)
        d.pop("repeat_password")
        return d


class UserDB(BaseUser):
    password_hash: str

    def __init__(self, **data):
        super().__init__(**data)
        self.password = None

    def model_dump(self, **kwargs):
        d = super().model_dump(**kwargs)
        d.pop("password_hash")
        return d
