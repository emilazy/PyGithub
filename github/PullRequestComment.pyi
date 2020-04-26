from datetime import datetime
from typing import Any, Dict

from github.GithubObject import CompletableGithubObject
from github.NamedUser import NamedUser
from github.PaginatedList import PaginatedList
from github.Reaction import Reaction

class PullRequestComment(CompletableGithubObject):
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
    @property
    def diff_hunk(self) -> str: ...
    def edit(self, body: str) -> None: ...
    def get_reactions(self) -> PaginatedList: ...
    @property
    def html_url(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def in_reply_to_id(self) -> int: ...
    @property
    def original_commit_id(self) -> str: ...
    @property
    def original_position(self) -> int: ...
    @property
    def path(self) -> str: ...
    @property
    def position(self) -> int: ...
    @property
    def pull_request_url(self) -> str: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
    @property
    def user(self) -> NamedUser: ...
