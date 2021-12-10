from typing import Optional, _UnionGenericAlias  # type: ignore

from pydantic import UUID4, BaseModel

from starlite import Partial


class Person(BaseModel):
    first_name: str
    last_name: str
    id: UUID4
    optional: Optional[str]


def test_partial():
    partial = Partial[Person]
    assert partial
    for field in partial.__fields__.values():
        assert field.allow_none
        assert not field.required
    for field in partial.__annotations__.values():
        assert isinstance(field, _UnionGenericAlias)
        assert type(None) in field.__args__