# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .tool_call import ToolCall

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TranscriptEntry(pydantic.BaseModel):
    role: str = pydantic.Field(description="the role of the speaker in the transcript")
    content: typing.Optional[str] = pydantic.Field(description="the content of what was spoken")
    name: typing.Optional[str] = pydantic.Field(description="the name of the speaker, if available")
    tool_call_id: typing.Optional[str] = pydantic.Field(
        description="the unique identifier for a tool call within this entry"
    )
    tool_calls: typing.Optional[typing.List[ToolCall]] = pydantic.Field(
        description="a list of tool calls associated with this transcript entry"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
