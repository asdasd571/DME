# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.dme_type_related_capabilities import DmeTypeRelatedCapabilities
from openapi_server.models.problem_details import ProblemDetails


class BaseRegisteredDMETypeProductionCapabilitiesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseRegisteredDMETypeProductionCapabilitiesApi.subclasses = BaseRegisteredDMETypeProductionCapabilitiesApi.subclasses + (cls,)
    async def production_capabilities_post(
        self,
        dme_type_related_capabilities: DmeTypeRelatedCapabilities,
    ) -> DmeTypeRelatedCapabilities:
        """To register DME type production capabilities"""
        ...
