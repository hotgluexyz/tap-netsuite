from netsuitesdk.internal.client import NetSuiteClient


class ExtendedNetSuiteClient(NetSuiteClient):
    def __init__(self, account=None, caching=True, caching_timeout=2592000):
        NetSuiteClient.__init__(self, account, caching, caching_timeout)
        # self.set_search_preferences(page_size=100, return_search_columns=True)
        self._search_preferences = self.SearchPreferences(
            bodyFieldsOnly=False,
            pageSize=100,
            returnSearchColumns=True
        )
