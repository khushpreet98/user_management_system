from click import DateTime
from mypy_extensions import TypedDict


class UserInterface(TypedDict, total=False):
    id: int
    first_name: str
    last_name: str
    full_name: str
    salary: int
    address :str
    created_at :DateTime


