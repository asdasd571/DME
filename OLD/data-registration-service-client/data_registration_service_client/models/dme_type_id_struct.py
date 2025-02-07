from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DmeTypeIdStruct")


@_attrs_define
class DmeTypeIdStruct:
    """Defining the attributes of DME type identifier

    Attributes:
        namespace (Union[Unset, str]): Indicating the entity responsible for the DME type definition.
        name (Union[Unset, str]): Name of the DME type. The string can be any character except “:“ (colon)
        version (Union[Unset, str]): Version of the DME type. The versioning and allowed characters are according to
            SemVer [11]
    """

    namespace: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace = self.namespace

        name = self.name

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        namespace = d.pop("namespace", UNSET)

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        dme_type_id_struct = cls(
            namespace=namespace,
            name=name,
            version=version,
        )

        dme_type_id_struct.additional_properties = d
        return dme_type_id_struct

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
