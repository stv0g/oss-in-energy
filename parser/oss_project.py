from dataclasses import dataclass
from typing import Optional, List
import validators
from datetime import date

# TODO: ist this a good approach?
# class Category(Enum):
#     MODELING
#     SIMULATION
#     INTERFACES
#     PLATFORM
#     FORECASTING
#     STATE_ESTIMATION
#     OPTIMIZATION
#     POWER_QUALITY
#     FIRMWARE
#     ALGORITHMS


@dataclass
class OpenSourceProject:
    """Class for keeping track of an item in inventory."""

    # mandatory
    name: str
    repository: str
    description: str

    # optional
    homepage: Optional[str]

    # auto generated if not given
    license: str
    languages: Optional[List[str]]
    tags: Optional[List[str]]

    # auto generated
    # category: str
    last_update: str
    last_release: Optional[date]
    first_release: Optional[date]

    # Ideas:
    # Contributors
    # CI/Coverage

    @classmethod
    def from_dict(cls, d: dict) -> "OpenSourceProject":
        # Mandatory
        if "name" in d and d["name"]:
            name = d["name"]
        else:
            raise Exception("Project needs to have a name!")

        if "repository" in d:
            repository = d["repository"]
        else:
            raise Exception("Project needs to have a valid url!")

        if "description" in d and d["description"]:
            description = d["description"]
        else:
            raise Exception("Project needs to have a proper description!")

        # Optional
        if "homepage" in d and validators.url(d["homepage"]):
            homepage = d["homepage"]
        else:
            homepage = None

        # Semi autogenerated
        if "license" in d and d["license"]:
            # TODO: Validate license against enum
            license = d["license"]
        else:
            # TODO: get license from API
            license = None

        if "languages" in d and d["language"]:
            # TODO: Convert to list
            languages = d["language"]
        else:
            # TODO: get languages from API
            languages = None

        if "tags" in d and d["tags"]:
            # TODO: Convert to list
            tags = d["tags"]
        else:
            # TODO: get tagss from API
            tags = None

        # TODO: generate from API
        last_update = None
        last_release = None
        first_release = None

        return cls(
            name=name,
            repository=repository,
            description=description,
            homepage=homepage,
            license=license,
            languages=languages,
            tags=tags,
            # category=category,
            last_update=last_update,
            last_release=last_release,
            first_release=first_release,
        )

    @classmethod
    def list_headers(cls):
        return [
            "Project",
            "Repository URL",
            "Description",
            "Homepage",
            "License",
            "Languages",
            "Tags",
            # "Category",
            "Last Update",
            "Last Release",
            "First Release",
        ]

    def to_list(self) -> List[str]:
        def stringify (o):
            if o:
                str(o)
            else:
                ""
        return [
            self.name,
            f'<a href="{self.repository}">{self.repository}</a>',
            self.description,
            f'<a href="{self.homepage}">{self.homepage}</a>',
            self.license,
            stringify(self.languages),
            stringify(self.tags),
            # self.category,
            stringify(self.last_update),
            stringify(self.last_release),
            stringify(self.first_release),
        ]
