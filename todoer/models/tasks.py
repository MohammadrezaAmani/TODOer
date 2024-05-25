from datetime import datetime
from typing import List, Literal

from todoer.models.base import Base
from todoer.models.user import BaseUser


class Tag(Base):
    name: str
    slug: str


class Task(Base):
    title: str
    description: str
    tags: List[Tag]
    due_date: datetime
    completed: bool
    owner: BaseUser
    users: List[BaseUser]


class Project(Base):
    name: str
    description: str
    owner: BaseUser
    users: List[BaseUser]
    tasks: List[Task]
    tags: List[Tag]
    due_date: datetime
    completed: bool = False
    completed_at: datetime | None = None


class Team(Base):
    name: str
    description: str
    owner: BaseUser
    users: List[BaseUser]
    projects: List[Project]
    tags: List[Tag]
    status: Literal["active", "inactive", "archived"]
