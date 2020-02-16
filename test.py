from unittest import TestCase
from uuid import UUID

from eventsourcing.application.sqlalchemy import SQLAlchemyApplication

from federatedwiki.application import FederatedWikiApplication


class TestApplication(TestCase):
    def test(self):
        # Construct application.
        with FederatedWikiApplication.mixin(SQLAlchemyApplication)() as app:
            # Start new page.
            page_id = app.start_new_page(
                title="Welcome Visitors", slug="welcome-visitors"
            )

            # Check we got a page ID.
            self.assertIsInstance(page_id, UUID)

            # Present page identified by the given slug.
            page_dict = app.present_page(slug="welcome-visitors")

            # Check we got a dict that has the given title.
            self.assertIsInstance(page_dict, dict)
            self.assertEqual(page_dict["title"], "Welcome Visitors")
