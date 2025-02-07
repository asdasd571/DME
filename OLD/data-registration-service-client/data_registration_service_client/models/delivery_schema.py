from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schema_types import SchemaTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeliverySchema")


@_attrs_define
class DeliverySchema:
    """Delivery schema for a DME type

    Attributes:
        type_ (Union[Unset, SchemaTypes]): Type of the schema supported by Data Producers
        delivery_schema_id (Union[Unset, str]): A Data Producer may support one or more delivery schemas and for each
            supported schema type a delivery schema identifier is assigned. A Data Consumer uses this attribute while
            creating a data job and request to deliver the data using specific schema type which is identified by this
            attribute.
        schema (Union[Unset, str]): The schema serialized to string. If this attribute is not present, the schema is
            assumed to be known from the DME type definition that is referenced by dmeTypeId
    """

    type_: Union[Unset, SchemaTypes] = UNSET
    delivery_schema_id: Union[Unset, str] = UNSET
    schema: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        delivery_schema_id = self.delivery_schema_id

        schema = self.schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if delivery_schema_id is not UNSET:
            field_dict["deliverySchemaId"] = delivery_schema_id
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, SchemaTypes]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SchemaTypes(_type_)

        delivery_schema_id = d.pop("deliverySchemaId", UNSET)

        schema = d.pop("schema", UNSET)

        delivery_schema = cls(
            type_=type_,
            delivery_schema_id=delivery_schema_id,
            schema=schema,
        )

        delivery_schema.additional_properties = d
        return delivery_schema

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
