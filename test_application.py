from unittest import TestCase
from uuid import UUID

from eventsourcing.application.sqlalchemy import SQLAlchemyApplication

from federatedwiki.application import FederatedWikiApplication


class TestApplication(TestCase):
    def test_application(self):
        # Construct application.
        with FederatedWikiApplication.mixin(SQLAlchemyApplication)() as app:
            assert isinstance(app, FederatedWikiApplication)

            # Start new page.
            page_id = app.start_new_page(
                title="Welcome Visitors", slug="welcome-visitors"
            )

            # Check we got a page ID.
            self.assertIsInstance(page_id, UUID)

            # Present page identified by the given slug.
            page = app.get_page(slug="welcome-visitors")

            # Check we got a dict that has the given title.
            self.assertIsInstance(page, dict)
            self.assertEqual(page["title"], "Welcome Visitors")

            # Append a paragraph.
            paragraph = "I am a paragraph"
            app.append_paragraph(slug="welcome-visitors", paragraph=paragraph)

            # Check the page has the paragraph.
            page = app.get_page(slug="welcome-visitors")
            self.assertEqual(page["paragraphs"][0], paragraph)
