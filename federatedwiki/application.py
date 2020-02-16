from eventsourcing.application.simple import SimpleApplication

from federatedwiki.domainmodel import WikiPage, create_index_entry_id, IndexEntry


class FederatedWikiApplication(SimpleApplication):
    def start_new_page(self, title, slug):
        page = WikiPage.start_new(
            title=title,
            slug=slug,
        )
        index_entry = IndexEntry.__create__(
            originator_id=create_index_entry_id(slug),
            page_id=page.id,
        )
        self.save([page, index_entry])
        return page.id

    def present_page(self, slug):
        index_entry_id = create_index_entry_id(slug)
        index_entry = self.get_index_entry(index_entry_id)
        page_id = index_entry.page_id
        page = self.get_page(page_id)
        page_dict = {
            'title': page.title
        }
        return page_dict

    def get_index_entry(self, index_entry_id) -> IndexEntry:
        try:
            index_entry = self.repository[index_entry_id]
            assert isinstance(index_entry, IndexEntry)
            return index_entry
        except KeyError:
            pass

    def get_page(self, page_id):
        try:
            page = self.repository[page_id]
            assert isinstance(page, WikiPage)
            return page
        except KeyError:
            pass
