from uuid import uuid5, NAMESPACE_URL

from eventsourcing.domain.model.aggregate import BaseAggregateRoot


class WikiPage(BaseAggregateRoot):
    @classmethod
    def start_new(self, title, slug):
        return self.__create__(title=title, slug=slug)

    def __init__(self, *, title, slug, **kwargs):
        super(WikiPage, self).__init__(**kwargs)
        self.title = title
        self.slug = slug


class IndexEntry(BaseAggregateRoot):
    def __init__(self, *, page_id, **kwargs):
        super(IndexEntry, self).__init__(**kwargs)
        self.page_id = page_id


def create_index_entry_id(slug):
    return uuid5(NAMESPACE_URL, f'/slug/{slug}')
