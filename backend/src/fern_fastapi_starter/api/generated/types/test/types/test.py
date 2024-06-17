# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import typing_extensions

from ....core.datetime_utils import serialize_datetime
from .exact_match_test import ExactMatchTest
from .json_validity_test import JsonValidityTest
from .regex_test import RegexTest
from .semantic_similarity_test import SemanticSimilarityTest
from pydantic import ConfigDict

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def exact_match(self, value: ExactMatchTest) -> Test:
        return Test(__root__=_Test.ExactMatch(**value.dict(exclude_unset=True), test_type="exact_match"))

    def regex(self, value: RegexTest) -> Test:
        return Test(__root__=_Test.Regex(**value.dict(exclude_unset=True), test_type="regex"))

    def semantic_similarity(self, value: SemanticSimilarityTest) -> Test:
        return Test(
            __root__=_Test.SemanticSimilarity(**value.dict(exclude_unset=True), test_type="semantic_similarity")
        )

    def json_validity(self, value: JsonValidityTest) -> Test:
        return Test(__root__=_Test.JsonValidity(**value.dict(exclude_unset=True), test_type="json_validity"))


class Test(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_Test.ExactMatch, _Test.Regex, _Test.SemanticSimilarity, _Test.JsonValidity]:
        return self.__root__

    def visit(
        self,
        exact_match: typing.Callable[[ExactMatchTest], T_Result],
        regex: typing.Callable[[RegexTest], T_Result],
        semantic_similarity: typing.Callable[[SemanticSimilarityTest], T_Result],
        json_validity: typing.Callable[[JsonValidityTest], T_Result],
    ) -> T_Result:
        if self.__root__.test_type == "exact_match":
            return exact_match(ExactMatchTest(**self.__root__.dict(exclude_unset=True, exclude={"TestType"})))
        if self.__root__.test_type == "regex":
            return regex(RegexTest(**self.__root__.dict(exclude_unset=True, exclude={"TestType"})))
        if self.__root__.test_type == "semantic_similarity":
            return semantic_similarity(
                SemanticSimilarityTest(**self.__root__.dict(exclude_unset=True, exclude={"TestType"}))
            )
        if self.__root__.test_type == "json_validity":
            return json_validity(JsonValidityTest(**self.__root__.dict(exclude_unset=True, exclude={"TestType"})))

    __root__: typing_extensions.Annotated[
        typing.Union[_Test.ExactMatch, _Test.Regex, _Test.SemanticSimilarity, _Test.JsonValidity],
        pydantic.Field(discriminator="test_type"),
    ]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)
    # TODO[pydantic]: The following keys were removed: `json_encoders`.
    # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
    model_config = ConfigDict(extra=pydantic.Extra.forbid, json_encoders={dt.datetime: serialize_datetime})


class _Test:
    class ExactMatch(ExactMatchTest):
        test_type: typing_extensions.Literal["exact_match"] = pydantic.Field(alias="TestType")
        model_config = ConfigDict(populate_by_name=True)

    class Regex(RegexTest):
        test_type: typing_extensions.Literal["regex"] = pydantic.Field(alias="TestType")
        model_config = ConfigDict(populate_by_name=True)

    class SemanticSimilarity(SemanticSimilarityTest):
        test_type: typing_extensions.Literal["semantic_similarity"] = pydantic.Field(alias="TestType")
        model_config = ConfigDict(populate_by_name=True)

    class JsonValidity(JsonValidityTest):
        test_type: typing_extensions.Literal["json_validity"] = pydantic.Field(alias="TestType")
        model_config = ConfigDict(populate_by_name=True)


Test.update_forward_refs()
