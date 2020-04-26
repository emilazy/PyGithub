from datetime import datetime
from typing import Any, Dict, Optional

from github.GithubObject import CompletableGithubObject
from github.NamedUser import NamedUser
from github.PaginatedList import PaginatedList
from github.Reaction import Reaction

class CommitComment(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def body(self) -> str: ...
    @property
    def commit_id(self) -> str: ...
    def create_reaction(self, reaction_type: str) -> Reaction: ...
    @property
    def created_at(self) -> datetime: ...
    def delete(self) -> None: ...
    def edit(self, body: str) -> None: ...
    def get_reactions(self) -> PaginatedList: ...
    @property
    def html_url(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def line(self) -> Optional[int]: ...
    @property
    def path(self) -> Optional[str]: ...
    @property
    def position(self) -> Optional[int]: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
    @property
    def user(self) -> NamedUser: ...
