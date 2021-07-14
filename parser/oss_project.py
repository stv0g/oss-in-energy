from dataclasses import dataclass
from typing import Optional, List


@dataclass
class OpenSourceProject:
    """Class for keeping track of an item in inventory."""

    name: str
    repository: str
    languages: Optional[List[str]]

    @classmethod
    def from_dict(cls, d: dict):
        if "name" in d:
            name = d["name"]
        else:
            name = "PeterPan"

        if "repository" in d:
            repo = d["repository"]
        else:
            repo = "https://example.com"

        return cls(name=name, repository=repo, languages=None)
