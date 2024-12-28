from __future__ import annotations

from typing import override

from model import Link
from ui.links_tree_control import LinkTreeControl


class ProjectLinksTreeControl(LinkTreeControl):
    def __init__(self, project_links: list[Link], *args, **kwargs):
        super().__init__(links=project_links, *args, **kwargs)

    @override
    @property
    def section_header(self):
        return "Projects"

    @override
    @property
    def is_empty(self):
        return False
