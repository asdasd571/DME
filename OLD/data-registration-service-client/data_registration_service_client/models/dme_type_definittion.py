from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delivery_schema import DeliverySchema
    from ..models.dme_type_definittion_data_production_schema import DmeTypeDefinittionDataProductionSchema
    from ..models.dme_type_id_struct import DmeTypeIdStruct
    from ..models.metadata import Metadata


T = TypeVar("T", bound="DmeTypeDefinittion")


@_attrs_define
class DmeTypeDefinittion:
    """Information of the DME type

    Attributes:
        dme_type_id (Union[Unset, DmeTypeIdStruct]): Defining the attributes of DME type identifier
        metadata (Union[Unset, Metadata]): Metadata that can be used in discovering the DME type
        data_production_schema (Union[Unset, DmeTypeDefinittionDataProductionSchema]): Schema that defines the
            information necessary to formulate a data request or data subscription.   If this attribute is not present, the
            schema is assumed to be known from the DME type definition that is referenced by dmeTypeId
        data_delivery_schemas (Union[Unset, list['DeliverySchema']]): List of delivery schemas supported by the producer
            for the DME type being registered.
        data_delivery_mechanisms (Union[Unset, list[Any]]): Defining the delivery mechanism supported by Data Producer
    """

    dme_type_id: Union[Unset, "DmeTypeIdStruct"] = UNSET
    metadata: Union[Unset, "Metadata"] = UNSET
    data_production_schema: Union[Unset, "DmeTypeDefinittionDataProductionSchema"] = UNSET
    data_delivery_schemas: Union[Unset, list["DeliverySchema"]] = UNSET
    data_delivery_mechanisms: Union[Unset, list[Any]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dme_type_id: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dme_type_id, Unset):
            dme_type_id = self.dme_type_id.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        data_production_schema: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_production_schema, Unset):
            data_production_schema = self.data_production_schema.to_dict()

        data_delivery_schemas: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data_delivery_schemas, Unset):
            data_delivery_schemas = []
            for data_delivery_schemas_item_data in self.data_delivery_schemas:
                data_delivery_schemas_item = data_delivery_schemas_item_data.to_dict()
                data_delivery_schemas.append(data_delivery_schemas_item)

        data_delivery_mechanisms: Union[Unset, list[Any]] = UNSET
        if not isinstance(self.data_delivery_mechanisms, Unset):
            data_delivery_mechanisms = []
            for data_delivery_mechanisms_item_data in self.data_delivery_mechanisms:
                data_delivery_mechanisms_item: Any
                data_delivery_mechanisms_item = data_delivery_mechanisms_item_data
                data_delivery_mechanisms.append(data_delivery_mechanisms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dme_type_id is not UNSET:
            field_dict["dmeTypeId"] = dme_type_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if data_production_schema is not UNSET:
            field_dict["dataProductionSchema"] = data_production_schema
        if data_delivery_schemas is not UNSET:
            field_dict["dataDeliverySchemas"] = data_delivery_schemas
        if data_delivery_mechanisms is not UNSET:
            field_dict["dataDeliveryMechanisms"] = data_delivery_mechanisms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.delivery_schema import DeliverySchema
        from ..models.dme_type_definittion_data_production_schema import DmeTypeDefinittionDataProductionSchema
        from ..models.dme_type_id_struct import DmeTypeIdStruct
        from ..models.metadata import Metadata

        d = src_dict.copy()
        _dme_type_id = d.pop("dmeTypeId", UNSET)
        dme_type_id: Union[Unset, DmeTypeIdStruct]
        if isinstance(_dme_type_id, Unset):
            dme_type_id = UNSET
        else:
            dme_type_id = DmeTypeIdStruct.from_dict(_dme_type_id)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Metadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Metadata.from_dict(_metadata)

        _data_production_schema = d.pop("dataProductionSchema", UNSET)
        data_production_schema: Union[Unset, DmeTypeDefinittionDataProductionSchema]
        if isinstance(_data_production_schema, Unset):
            data_production_schema = UNSET
        else:
            data_production_schema = DmeTypeDefinittionDataProductionSchema.from_dict(_data_production_schema)

        data_delivery_schemas = []
        _data_delivery_schemas = d.pop("dataDeliverySchemas", UNSET)
        for data_delivery_schemas_item_data in _data_delivery_schemas or []:
            data_delivery_schemas_item = DeliverySchema.from_dict(data_delivery_schemas_item_data)

            data_delivery_schemas.append(data_delivery_schemas_item)

        data_delivery_mechanisms = []
        _data_delivery_mechanisms = d.pop("dataDeliveryMechanisms", UNSET)
        for data_delivery_mechanisms_item_data in _data_delivery_mechanisms or []:

            def _parse_data_delivery_mechanisms_item(data: object) -> Any:
                return cast(Any, data)

            data_delivery_mechanisms_item = _parse_data_delivery_mechanisms_item(data_delivery_mechanisms_item_data)

            data_delivery_mechanisms.append(data_delivery_mechanisms_item)

        dme_type_definittion = cls(
            dme_type_id=dme_type_id,
            metadata=metadata,
            data_production_schema=data_production_schema,
            data_delivery_schemas=data_delivery_schemas,
            data_delivery_mechanisms=data_delivery_mechanisms,
        )

        dme_type_definittion.additional_properties = d
        return dme_type_definittion

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
