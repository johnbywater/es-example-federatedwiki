from unittest import TestCase
from uuid import UUID

from eventsourcing.application.sqlalchemy import SQLAlchemyApplication

from federatedwiki.application import FederatedWikiApplication


class TestApplication(TestCase):
    def test(self):
        # Construct application.
        with FederatedWikiApplication.mixin(SQLAlchemyApplication)() as app:
            self.assertIsInstance(app, FederatedWikiApplication)

            # Start new page.
            page_id = app.start_new_page()
            self.assertIsInstance(page_id, UUID)


