from unittest import TestCase
from uuid import uuid4

from eventsourcing.application.sqlalchemy import SQLAlchemyApplication

from federatedwiki.application import FederatedWikiApplication


class TestApplication(TestCase):
    def test(self):
        # Construct application.
        with FederatedWikiApplication.mixin(SQLAlchemyApplication)() as app:
            self.assertIsInstance(app, FederatedWikiApplication)
