#!/usr/bin/env python3
""" Client Testing """
from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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


@parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
    )
class TestIntegrationGithubOrgClient(TestCase):
    """ Github intergration test class """
    @classmethod
    def setUpClass(self):
        """ Set up class """
        self.get_patcher = patch("utils.requests")
        request_mock = self.get_patcher.start()
        get_mock = MagicMock()
        json_mock = MagicMock()
        get_mock.json = json_mock

        def get_side_effect(url):
            if url == GithubOrgClient.ORG_URL.format(org="google"):
                json_mock.return_value = self.org_payload
            if url == self.org_payload["repos_url"]:
                json_mock.return_value = self.repos_payload
            return get_mock
        get_mock.side_effect = get_side_effect
        request_mock.get = get_mock

    @classmethod
    def tearDownClass(self):
        """ TestCase teardown method """
        self.get_patcher.stop()

    def test_public_repos(self):
        """ tests public repos """
        new_github_test = GithubOrgClient("google")
        repos = new_github_test.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """ Test public repo filter by license """
        new_github_test = GithubOrgClient("google")
        repos = new_github_test.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
