from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import (
    Column, String
)

from test_data_service.apps.models.abstract import IDBase


class TestData(IDBase):
    __tablename__ = "test_data"

    key = Column(String(128))
    value = Column(JSONB)
