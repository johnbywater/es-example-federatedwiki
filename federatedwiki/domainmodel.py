from eventsourcing.domain.model.aggregate import AggregateRoot


class WikiPage(AggregateRoot):
    @classmethod
    def start_new(self):
        return self.__create__()
