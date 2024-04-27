#!/usr/bin/env python3
""" Client Testing """
from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """ Testing http client """
    @parameterized.expand([
            ("google",),
            ("abc",)
        ])
    @patch('client.get_json')
    def test_org(self, org, json_mock):
        """ testing org method """
        json_mock.return_value = None
        inst = GithubOrgClient(org)
        inst.org
        req_url = inst.ORG_URL.format(org=org)
        json_mock.assert_called_once_with(req_url)

    def test_public_repos_url(self):
        """ test puvli url """
        with patch.object(GithubOrgClient, 'org') as org_mock:
            org_mock.return_value = {'repos_url': 'makeint'}
            new_test = GithubOrgClient("maker")
            new_test.org
            self.assertEqual(new_test._public_repos_url, "makeint")
