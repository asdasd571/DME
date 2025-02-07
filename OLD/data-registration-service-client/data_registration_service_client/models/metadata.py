from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Metadata")


@_attrs_define
class Metadata:
    """Metadata that can be used in discovering the DME type

    Attributes:
        data_category (Union[Unset, list[str]]): Defines the category of the DME type e.g., PM counters
        rat (Union[Unset, list[str]]): Defines the radio access technology e.g., 5G
    """

    data_category: Union[Unset, list[str]] = UNSET
    rat: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_category: Union[Unset, list[str]] = UNSET
        if not isinstance(self.data_category, Unset):
            data_category = self.data_category

        rat: Union[Unset, list[str]] = UNSET
        if not isinstance(self.rat, Unset):
            rat = self.rat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_category is not UNSET:
            field_dict["dataCategory"] = data_category
        if rat is not UNSET:
            field_dict["rat"] = rat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        data_category = cast(list[str], d.pop("dataCategory", UNSET))

        rat = cast(list[str], d.pop("rat", UNSET))

        metadata = cls(
            data_category=data_category,
            rat=rat,
        )

        metadata.additional_properties = d
        return metadata

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
