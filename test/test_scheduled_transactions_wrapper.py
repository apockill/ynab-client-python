# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ynab_client
from ynab_client.models.scheduled_transactions_wrapper import ScheduledTransactionsWrapper  # noqa: E501
from ynab_client.rest import ApiException


class TestScheduledTransactionsWrapper(unittest.TestCase):
    """ScheduledTransactionsWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScheduledTransactionsWrapper(self):
        """Test ScheduledTransactionsWrapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ynab_client.models.scheduled_transactions_wrapper.ScheduledTransactionsWrapper()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
