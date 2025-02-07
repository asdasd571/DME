from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KafkaDeliveryConfiguration")


@_attrs_define
class KafkaDeliveryConfiguration:
    """These configuration will be applied if KAFKA_DATA_STREAM is selected as delivery method

    Attributes:
        num_partitions (Union[Unset, int]): Number of partitions
        clean_up_policy (Union[Unset, str]): cleanUpPolicy is based on cleanup.policy defined in the Kafka Documentation
            [15].
        compression_type (Union[Unset, str]):  compressionType is based on compression.type defined in the Kafka
            Documentation [15] .
        retention_bytes (Union[Unset, int]):  retentionBytes is based on retention.bytes defined in the Kafka
            Documentation [15] . This attribute is applicable ONLY when cleanUpPolicy is set to DELETE
        retention_ms (Union[Unset, int]):  retentionMs is based on retention.ms defined in the Kafka Documentation [15]
            . This attribute is applicable ONLY when cleanUpPolicy is set to DELETE
    """

    num_partitions: Union[Unset, int] = UNSET
    clean_up_policy: Union[Unset, str] = UNSET
    compression_type: Union[Unset, str] = UNSET
    retention_bytes: Union[Unset, int] = UNSET
    retention_ms: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        num_partitions = self.num_partitions

        clean_up_policy = self.clean_up_policy

        compression_type = self.compression_type

        retention_bytes = self.retention_bytes

        retention_ms = self.retention_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_partitions is not UNSET:
            field_dict["numPartitions"] = num_partitions
        if clean_up_policy is not UNSET:
            field_dict["cleanUpPolicy"] = clean_up_policy
        if compression_type is not UNSET:
            field_dict["compressionType"] = compression_type
        if retention_bytes is not UNSET:
            field_dict["retentionBytes"] = retention_bytes
        if retention_ms is not UNSET:
            field_dict["retentionMs"] = retention_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        num_partitions = d.pop("numPartitions", UNSET)

        clean_up_policy = d.pop("cleanUpPolicy", UNSET)

        compression_type = d.pop("compressionType", UNSET)

        retention_bytes = d.pop("retentionBytes", UNSET)

        retention_ms = d.pop("retentionMs", UNSET)

        kafka_delivery_configuration = cls(
            num_partitions=num_partitions,
            clean_up_policy=clean_up_policy,
            compression_type=compression_type,
            retention_bytes=retention_bytes,
            retention_ms=retention_ms,
        )

        kafka_delivery_configuration.additional_properties = d
        return kafka_delivery_configuration

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
