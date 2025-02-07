from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DmeTypeDefinittionDataProductionSchema")


@_attrs_define
class DmeTypeDefinittionDataProductionSchema:
    """Schema that defines the information necessary to formulate a data request or data subscription.   If this attribute
    is not present, the schema is assumed to be known from the DME type definition that is referenced by dmeTypeId

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        dme_type_definittion_data_production_schema = cls()

        dme_type_definittion_data_production_schema.additional_properties = d
        return dme_type_definittion_data_production_schema

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
