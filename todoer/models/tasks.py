from datetime import datetime
from typing import List

from todoer.models.base import Base


class Tag(Base):
    name: str
    slug: str


class Task(Base):
    title: str
    description: str
    tags: List[Tag]
    due_date: datetime
    completed: bool
