from test_data_service.apps.models.base import SyncPostgresDriver
from test_data_service.apps.models.models import TestData


class BaseProvider:
    def __init__(self):
        self.session = SyncPostgresDriver().session()


class TestDataProvider(BaseProvider):
    def add(self, test_data: TestData):
        self.session.add(test_data)
        self.session.commit()
