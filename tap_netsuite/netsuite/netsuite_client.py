from netsuitesdk.internal.client import NetSuiteClient

from zeep.exceptions import LookupError as ZeepLookupError
class ExtendedNetSuiteClient(NetSuiteClient):
    def __init__(self, account=None, fetch_child=True, caching=True, caching_timeout=2592000):
        NetSuiteClient.__init__(self, account, caching, caching_timeout)
        # self.set_search_preferences(page_size=100, return_search_columns=True)
        self._search_preferences = self.SearchPreferences(
            bodyFieldsOnly=not(fetch_child),
            pageSize=500,
            returnSearchColumns=True
        )
        self._init_complex_types()
    
    def _init_complex_types(self):
        """
        Adds custom complex type for contacts.
        Based on: https://webservices.netsuite.com/xsd/platform/v2017_2_0/common.xsd
        """
        # TODO: Extend this to support other complex types and namespaces, making we
        # less dependent on the NetSuite API SDK.
        super()._init_complex_types()
        namespace = "ns5"
        type_name = "ContactSearchBasic"
        verbose_type_name = '{}:{}'.format(namespace, type_name)
        try:
            complex_type = self._client.get_type(verbose_type_name)
        except ZeepLookupError:
            self.logger.warning('LookupError: Did not find complex type {}'.format(type_name))
        else:
            setattr(self, type_name, complex_type)
            self._complex_types[type_name] = complex_type
            self._namespaces[namespace].append(complex_type)