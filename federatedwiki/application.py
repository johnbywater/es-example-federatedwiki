from uuid import UUID

from eventsourcing.application.simple import SimpleApplication

from federatedwiki.domainmodel import IndexEntry, WikiPage, create_index_entry_id


class FederatedWikiApplication(SimpleApplication):
    def start_new_page(self, title: str, slug: str):
        page = WikiPage.start_new(title=title, slug=slug,)
        index_entry = IndexEntry.__create__(
            originator_id=create_index_entry_id(slug), page_id=page.id,
        )
        self.save([page, index_entry])
        return page.id

    def present_page(self, slug: str):
        index_entry_id = create_index_entry_id(slug)
        index_entry = self._get_index_entry(index_entry_id)
        page_id = index_entry.page_id
        page = self._get_page(page_id)
        page_dict = {"title": page.title}
        return page_dict

    def _get_index_entry(self, index_entry_id: UUID) -> IndexEntry:
        index_entry = self.repository[index_entry_id]
        assert isinstance(index_entry, IndexEntry)
        return index_entry

    def _get_page(self, page_id: UUID) -> WikiPage:
        page = self.repository[page_id]
        assert isinstance(page, WikiPage)
        return page
