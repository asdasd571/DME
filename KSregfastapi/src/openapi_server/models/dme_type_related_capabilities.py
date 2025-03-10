# coding: utf-8

"""
    Data registration service

    API for Data registration service. © 2024, O-RAN ALLIANCE. All rights reserved. 

    The version of the OpenAPI document: 2.0.0-alpha.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_server.models.data_delivery_mode import DataDeliveryMode
from openapi_server.models.dme_type_definition import DmeTypeDefinition
from openapi_server.models.interface_description import InterfaceDescription
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DmeTypeRelatedCapabilities(BaseModel):
    """
    Information related to the registration as producer of a DME type
    """ # noqa: E501
    dme_type_definition: DmeTypeDefinition = Field(alias="dmeTypeDefinition")
    constraints: Optional[Dict[str, Any]] = Field(default=None, description="Formulates producer constraints or constraints applicable to the consumption related to the DME type based on the dataProductionSchema")
    data_access_endpoint: Optional[InterfaceDescription] = Field(alias="dataAccessEndpoint")
    data_delivery_modes: List[DataDeliveryMode] = Field(alias="dataDeliveryModes")
    __properties: ClassVar[List[str]] = ["dmeTypeDefinition", "constraints", "dataAccessEndpoint", "dataDeliveryModes"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DmeTypeRelatedCapabilities from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of dme_type_definition
        if self.dme_type_definition:
            _dict['dmeTypeDefinition'] = self.dme_type_definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_access_endpoint
        if self.data_access_endpoint:
            _dict['dataAccessEndpoint'] = self.data_access_endpoint.to_dict()
        # set to None if data_access_endpoint (nullable) is None
        # and model_fields_set contains the field
        if self.data_access_endpoint is None and "data_access_endpoint" in self.model_fields_set:
            _dict['dataAccessEndpoint'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DmeTypeRelatedCapabilities from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dmeTypeDefinition": DmeTypeDefinition.from_dict(obj.get("dmeTypeDefinition")) if obj.get("dmeTypeDefinition") is not None else None,
            "constraints": obj.get("constraints"),
            "dataAccessEndpoint": InterfaceDescription.from_dict(obj.get("dataAccessEndpoint")) if obj.get("dataAccessEndpoint") is not None else None,
            "dataDeliveryModes": obj.get("dataDeliveryModes")
        })
        return _obj


