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
            # self.assertEqual(new_test._public_repos_url, "makeint")

    @patch('client.get_json')
    def test_public_repos(self, json_mock):
        """ this is it"""
        get_json_repos = [
                {'name': 'first public'},
                {'name': 'second public'}
            ]
        json_mock.return_value = get_json_repos
        with patch.object(GithubOrgClient, '_public_repos_url') as org_mock:
            org_mock.return_value = "someething"
            new_test = GithubOrgClient("maker")
            new_test._public_repos_url()
            result = new_test.public_repos()
            self.assertEqual(result, ['first public', 'second public'])
            org_mock.assert_called_once()
            json_mock.assert_called_once()

    @parameterized.expand([
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license_key, expected):
        """ Test has license method """
        found_license = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(found_license, expected)
