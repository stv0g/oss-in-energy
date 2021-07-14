from dataclasses import dataclass
from typing import Optional, List


@dataclass
class OpenSourceProject:
    """Class for keeping track of an item in inventory."""

    name: str
    repository: str
    languages: Optional[List[str]]

    @classmethod
    def from_dict(cls, d: dict) -> 'OpenSourceProject':
        if "name" in d:
            name = d["name"]
        else:
            raise Exception("Project needs to have a name!")

        if "repository" in d:
            repo = d["repository"]
        else:
            repo = "https://example.com"

        return cls(name=name, repository=repo, languages=None)

    @classmethod
    def list_headers(cls):
        return ["Project", "Repository URL", "Languages"]

    def to_list(self) -> List[str]:
        return [self.name, f'<a href="{self.repository}">{self.repository}</a>' , str(self.languages)]