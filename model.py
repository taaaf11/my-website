from dataclasses import dataclass
from typing import Protocol


# nothing to do with `Animatable` in other languages
class Animatable(Protocol):
    def on_section_change(self) -> None:
        ...


# a link in link-tree
@dataclass
class Link:
    heading: str | None
    description: str
    url: str

    def __post_init__(self):
        if self.heading is None:
            self.heading = self.url
