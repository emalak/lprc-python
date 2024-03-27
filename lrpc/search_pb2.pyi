from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddLandmarkRequest(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class AddLandmarkResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SearchRequest(_message.Message):
    __slots__ = ("query",)
    QUERY_FIELD_NUMBER: _ClassVar[int]
    query: str
    def __init__(self, query: _Optional[str] = ...) -> None: ...

class SearchResponse(_message.Message):
    __slots__ = ("landmarkIds", "tagIds")
    LANDMARKIDS_FIELD_NUMBER: _ClassVar[int]
    TAGIDS_FIELD_NUMBER: _ClassVar[int]
    landmarkIds: _containers.RepeatedScalarFieldContainer[str]
    tagIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, landmarkIds: _Optional[_Iterable[str]] = ..., tagIds: _Optional[_Iterable[str]] = ...) -> None: ...
