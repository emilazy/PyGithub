from typing import Any, Dict, List, Union

from github.BranchProtection import BranchProtection
from github.Commit import Commit
from github.GithubObject import NonCompletableGithubObject, _NotSetType
from github.PaginatedList import PaginatedList
from github.RequiredPullRequestReviews import RequiredPullRequestReviews
from github.RequiredStatusChecks import RequiredStatusChecks

class Branch(NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    def add_required_signatures(self) -> None: ...
    @property
    def commit(self) -> Commit: ...
    def edit_protection(
        self,
        strict: Union[bool, _NotSetType] = ...,
        contexts: Union[List[str], _NotSetType] = ...,
        enforce_admins: Union[bool, _NotSetType] = ...,
        dismissal_users: Union[_NotSetType, List[str]] = ...,
        dismissal_teams: Union[_NotSetType, List[str]] = ...,
        dismiss_stale_reviews: Union[bool, _NotSetType] = ...,
        require_code_owner_reviews: Union[bool, _NotSetType] = ...,
        required_approving_review_count: Union[int, _NotSetType] = ...,
        user_push_restrictions: Union[_NotSetType, List[str]] = ...,
        team_push_restrictions: Union[_NotSetType, List[str]] = ...,
    ) -> None: ...
    def edit_required_pull_request_reviews(
        self,
        dismissal_users: Union[_NotSetType, List[str]] = ...,
        dismissal_teams: Union[_NotSetType, List[str]] = ...,
        dismiss_stale_reviews: Union[bool, _NotSetType] = ...,
        require_code_owner_reviews: Union[_NotSetType, bool] = ...,
        required_approving_review_count: Union[int, _NotSetType] = ...,
    ) -> None: ...
    def edit_required_status_checks(
        self,
        strict: Union[_NotSetType, bool] = ...,
        contexts: Union[List[str], _NotSetType] = ...,
    ) -> None: ...
    def edit_team_push_restrictions(self, *teams: str) -> None: ...
    def edit_user_push_restrictions(self, *users: str) -> None: ...
    def get_admin_enforcement(self) -> bool: ...
    def get_protection(self) -> BranchProtection: ...
    def get_required_pull_request_reviews(self) -> RequiredPullRequestReviews: ...
    def get_required_signatures(self) -> bool: ...
    def get_required_status_checks(self) -> RequiredStatusChecks: ...
    def get_team_push_restrictions(self) -> PaginatedList: ...
    def get_user_push_restrictions(self) -> PaginatedList: ...
    @property
    def name(self) -> str: ...
    @property
    def protected(self) -> bool: ...
    @property
    def protection_url(self) -> str: ...
    def remove_admin_enforcement(self) -> None: ...
    def remove_protection(self) -> None: ...
    def remove_push_restrictions(self) -> None: ...
    def remove_required_pull_request_reviews(self) -> None: ...
    def remove_required_signatures(self) -> None: ...
    def remove_required_status_checks(self) -> None: ...
    def set_admin_enforcement(self) -> None: ...
