from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProblemDetails")


@_attrs_define
class ProblemDetails:
    """A problem detail to carry details in an HTTP response according to RFC 7807

    Attributes:
        type_ (Union[Unset, str]): a URI reference according to IETF RFC 3986 that identifies the problem type
        title (Union[Unset, str]): human-readable summary of the problem type
        status (Union[Unset, float]): the HTTP status code
        detail (Union[Unset, str]): human-readable explanation
        instance (Union[Unset, str]): URI reference that identifies the specific occurrence of the problem
    """

    type_: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    status: Union[Unset, float] = UNSET
    detail: Union[Unset, str] = UNSET
    instance: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        title = self.title

        status = self.status

        detail = self.detail

        instance = self.instance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if detail is not UNSET:
            field_dict["detail"] = detail
        if instance is not UNSET:
            field_dict["instance"] = instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        type_ = d.pop("type", UNSET)

        title = d.pop("title", UNSET)

        status = d.pop("status", UNSET)

        detail = d.pop("detail", UNSET)

        instance = d.pop("instance", UNSET)

        problem_details = cls(
            type_=type_,
            title=title,
            status=status,
            detail=detail,
            instance=instance,
        )

        problem_details.additional_properties = d
        return problem_details

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
