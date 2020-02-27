from copy import copy
from uuid import UUID

from eventsourcing.application.simple import SimpleApplication
from eventsourcing.exceptions import RepositoryKeyError

from federatedwiki.domainmodel import IndexEntry, WikiPage, create_index_entry_id


class PageNotFound(Exception):
    pass


class FederatedWikiApplication(SimpleApplication):
    def start_new_page(self, title: str, slug: str):
        page = WikiPage.start_new(title=title, slug=slug,)
        index_entry = IndexEntry.__create__(
            originator_id=create_index_entry_id(slug), page_id=page.id,
        )
        self.save([page, index_entry])
        return page.id

    def get_page(self, slug: str):
        page_id = self._get_page_id_from_slug(slug)
        page = self._get_page(page_id)
        page_dict = {
            "title": page.title,
            "paragraphs": copy(page.paragraphs)
        }
        return page_dict

    def _get_page_id_from_slug(self, slug):
        index_entry_id = create_index_entry_id(slug)
        try:
            index_entry = self._get_index_entry(index_entry_id)
        except RepositoryKeyError:
            raise PageNotFound(slug)

        page_id = index_entry.page_id
        return page_id

    def _get_index_entry(self, index_entry_id: UUID) -> IndexEntry:
        index_entry = self.repository[index_entry_id]
        assert isinstance(index_entry, IndexEntry)
        return index_entry

    def _get_page(self, page_id: UUID) -> WikiPage:
        page = self.repository[page_id]
        assert isinstance(page, WikiPage)
        return page

    def append_paragraph(self, slug, paragraph):
        page_id = self._get_page_id_from_slug(slug)
        page = self._get_page(page_id)
        page.append_paragraph(paragraph)
        self.save([page])
