from uuid import NAMESPACE_URL, UUID, uuid5

from eventsourcing.domain.model.aggregate import BaseAggregateRoot
from eventsourcing.whitehead import T


class WikiPage(BaseAggregateRoot):
    @classmethod
    def start_new(cls: T, title, slug) -> T:
        return cls.__create__(title=title, slug=slug)

    def __init__(self, *, title: str, slug: str, **kwargs):
        super(WikiPage, self).__init__(**kwargs)
        self.title = title
        self.slug = slug


class IndexEntry(BaseAggregateRoot):
    def __init__(self, *, page_id: UUID, **kwargs):
        super(IndexEntry, self).__init__(**kwargs)
        self.page_id = page_id


def create_index_entry_id(slug: str) -> UUID:
    return uuid5(NAMESPACE_URL, f"/slug/{slug}")
