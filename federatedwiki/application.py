from eventsourcing.application.simple import SimpleApplication

from federatedwiki.domainmodel import WikiPage


class FederatedWikiApplication(SimpleApplication):
    def start_new_page(self):
        page = WikiPage.start_new()
        self.save([page])
        return page.id
