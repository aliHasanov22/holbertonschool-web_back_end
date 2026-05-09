#!/usr/bin/env python3
"""Unittests for client.py
"""

import unittest
from unittest import TestCase
from parameterized import parameterized, parameterized_class
from unittest.mock import Mock, PropertyMock, patch
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns correct value"""

        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, test_payload)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test that _public_repos_url returns repos_url from org"""

        payload = {"repos_url": "https://api.github.com/orgs/test/repos"}

        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("test")

            self.assertEqual(client._public_repos_url,
                             payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns repository names"""

        payload = [
            {"name": "repo_one"},
            {"name": "repo_two"},
        ]
        repos_url = "https://api.github.com/orgs/test/repos"
        mock_get_json.return_value = payload

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = repos_url
            client = GithubOrgClient("test")

            self.assertEqual(client.public_repos(),
                             ["repo_one", "repo_two"])

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns expected boolean"""

        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up class fixtures and mock requests.get"""

        cls.get_patcher = patch("requests.get")
        mock_get = cls.get_patcher.start()

        def get_payload(url):
            """Return a mocked response based on URL"""

            response = Mock()
            if url == "https://api.github.com/orgs/google":
                response.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                response.json.return_value = cls.repos_payload
            return response

        mock_get.side_effect = get_payload

    @classmethod
    def tearDownClass(cls):
        """Stop requests.get patcher"""

        cls.get_patcher.stop()
