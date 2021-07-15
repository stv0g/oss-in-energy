from datetime import datetime
from typing import Optional, Tuple
from urllib.parse import urlparse

from dateutil.parser import parse
from github import Github
from github.Repository import Repository

from project_types import Activity

# TODO: Potentially use an API Token from Environment variables here
github_api = Github()


class GithubRepo:
    url: str
    repo: Repository

    def __init__(self, url: str):
        parsed_url = urlparse(url)
        assert parsed_url.netloc == "github.com"
        assert len(parsed_url.path.split("/")) == 3

        repo = github_api.get_repo(parsed_url.path.lstrip("/"))
        self.url = url
        self.repo = repo

    def get_latest_release(self) -> Optional[Activity]:
        try:
            latest_release = self.repo.get_releases()[0]
            return Activity(latest_release.created_at.date(), latest_release.html_url)
        except IndexError:
            return None

    def get_first_release(self) -> Optional[Activity]:
        try:
            first_release = self.repo.get_releases()[0]
            return Activity(first_release.created_at.date(), first_release.html_url)
        except IndexError:
            return None

    def get_last_activity(self) -> Activity:
        last_commit = self.repo.get_commits()[0]
        date = parse(last_commit.last_modified).date()
        return Activity(date, last_commit.html_url)
