# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class TrunkTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks/TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "domain_name": "test.pstn.twilio.com",
                "disaster_recovery_method": "POST",
                "disaster_recovery_url": "http://disaster-recovery.com",
                "friendly_name": "friendly_name",
                "secure": false,
                "cnam_lookup_enabled": false,
                "recording": {
                    "mode": "do-not-record",
                    "trim": "do-not-trim"
                },
                "auth_type": "",
                "auth_type_set": [],
                "date_created": "2015-01-02T11:23:45Z",
                "date_updated": "2015-01-02T11:23:45Z",
                "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "origination_urls": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls",
                    "credential_lists": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists",
                    "ip_access_control_lists": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists",
                    "phone_numbers": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers"
                }
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks(sid="TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://trunking.twilio.com/v1/Trunks/TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.trunking.v1.trunks(sid="TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks.create()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://trunking.twilio.com/v1/Trunks',
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "domain_name": "test.pstn.twilio.com",
                "disaster_recovery_method": "POST",
                "disaster_recovery_url": "http://disaster-recovery.com",
                "friendly_name": "friendly_name",
                "secure": false,
                "cnam_lookup_enabled": false,
                "recording": {
                    "mode": "do-not-record",
                    "trim": "do-not-trim"
                },
                "auth_type": "",
                "auth_type_set": [],
                "date_created": "2015-01-02T11:23:45Z",
                "date_updated": "2015-01-02T11:23:45Z",
                "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "origination_urls": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls",
                    "credential_lists": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists",
                    "ip_access_control_lists": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists",
                    "phone_numbers": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers"
                }
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks.create()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trunking.twilio.com/v1/Trunks',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks?PageSize=50&Page=0",
                    "url": "https://trunking.twilio.com/v1/Trunks?PageSize=50&Page=0",
                    "page_size": 50,
                    "key": "trunks",
                    "next_page_url": null,
                    "page": 0,
                    "previous_page_url": null
                },
                "trunks": [
                    {
                        "sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "domain_name": "test.pstn.twilio.com",
                        "disaster_recovery_method": "POST",
                        "disaster_recovery_url": "http://disaster-recovery.com",
                        "friendly_name": "friendly_name",
                        "secure": false,
                        "cnam_lookup_enabled": false,
                        "recording": {
                            "mode": "do-not-record",
                            "trim": "do-not-trim"
                        },
                        "auth_type": "",
                        "auth_type_set": [],
                        "date_created": "2015-01-02T11:23:45Z",
                        "date_updated": "2015-01-02T11:23:45Z",
                        "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "origination_urls": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls",
                            "credential_lists": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists",
                            "ip_access_control_lists": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists",
                            "phone_numbers": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers"
                        }
                    }
                ]
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://trunking.twilio.com/v1/Trunks?PageSize=50&Page=0",
                    "url": "https://trunking.twilio.com/v1/Trunks?PageSize=50&Page=0",
                    "page_size": 50,
                    "key": "trunks",
                    "next_page_url": null,
                    "page": 0,
                    "previous_page_url": null
                },
                "trunks": []
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trunking.v1.trunks(sid="TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://trunking.twilio.com/v1/Trunks/TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "domain_name": "test.pstn.twilio.com",
                "disaster_recovery_method": "GET",
                "disaster_recovery_url": "http://updated-recovery.com",
                "friendly_name": "updated_name",
                "secure": true,
                "cnam_lookup_enabled": true,
                "recording": {
                    "mode": "do-not-record",
                    "trim": "do-not-trim"
                },
                "auth_type": "",
                "auth_type_set": [],
                "date_created": "2015-01-02T11:23:45Z",
                "date_updated": "2015-01-02T11:23:45Z",
                "url": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "origination_urls": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/OriginationUrls",
                    "credential_lists": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/CredentialLists",
                    "ip_access_control_lists": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IpAccessControlLists",
                    "phone_numbers": "https://trunking.twilio.com/v1/Trunks/TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/PhoneNumbers"
                }
            }
            '''
        ))

        actual = self.client.trunking.v1.trunks(sid="TRXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)