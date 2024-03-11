from dataclasses import dataclass

from src.domain.repository.abstract import IUserRepository, IContactRepository
from src.content import KeyboardManager


@dataclass
class RepositoryService:
    user_repository: IUserRepository
    contact_repository: IContactRepository


@dataclass
class ContentService:
    keyboards: KeyboardManager


@dataclass
class Services:
    repository: RepositoryService
    content: ContentService
